from flask import Flask, request, jsonify
from PIL import Image
import io, os
from google.cloud import vision
import datefinder

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'eventme-318812-c378b2f19c9b.json' # key needed for the authentification of Google Cloud services

app = Flask(__name__)

result = {} # initiate dictonary to store results

@app.route("/imgt", methods=["POST", "GET"])   # define the url and initiate the web application

def process_image():
    if request.method == 'POST':    
        file = request.files['image']   #image file is submitted to the server via POST request
        img = Image.open(file.stream)       
        img = img.save("saved.jpg")     #image is saved to the server overwriting a possibly existing image

    if os.stat("saved.jpg").st_size > 1000000:  # compress the image to less than 1 MB
        file_size = os.stat("saved.jpg").st_size  # determening size of the image in bytes
        quality = 60
        while file_size > 1000000:  
            img = Image.open("saved.jpg")  # open the imgae
            img.save("saved.jpg", optimize=True, quality=quality)  # lower the quality and overwrite the existing image
            file_size = os.stat("saved.jpg").st_size  # determine the new file size
            quality -= 10  # try with less quality

    client = vision.ImageAnnotatorClient()  # create instance of ImageAnnotatorClient to get access to the Cloud Vision image annotater service an its OCR functions
    with io.open("saved.jpg", 'rb') as image_file:  
       content = image_file.read()                  
    image = vision.Image(content=content) # open the previously saved image and send it to the Google Cloud servers
        
    response = client.text_detection(image=image)  
    text = response.text_annotations[0].description # use the text detection function of the ImageAnnotatorClient to extract text from the image as a string

    dates = datefinder.find_dates(text) # use the datefinder module to extract the date from the text as datetime objekt
    for n in dates: 
         dates= str(n) # convert datetime objekt into string

    date=""
    time=""
    for n in range(0, 10):  # seperate date and time
        date+=str(dates[n])
   

    for n in range(11,19):
        time+=str(dates[n])


    result.update({ "date": date, "time":time  }) # update the dictonary

        
      
    return jsonify(result) # return the result in json format 
    
    
@app.route('/') 
def index():    # display results on seperate url
    global result
    return result   
    


if __name__ == "__main__":
    app.run(debug=True) # start a debugger when running the app

