from flask import Flask, request, jsonify
from PIL import Image
import io, os
from google.cloud import vision
import datefinder




os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'eventme-318812-c378b2f19c9b.json'
app = Flask(__name__)
date= ""
result = {}


@app.route("/imgt", methods=["POST", "GET"])
def process_image():
    global result
    if request.method == 'POST':
        file = request.files['image']
        img = Image.open(file.stream)
        img = img.save("saved.jpg")
        

        client = vision.ImageAnnotatorClient()
        with io.open("saved.jpg", 'rb') as image_file:
           content = image_file.read()
        image = vision.Image(content=content)
        
        response = client.text_detection(image=image)
        text = response.text_annotations[0].description

        dates = datefinder.find_dates(text)
        for data in dates: 
             date= str(data) 
        result.update({ "date": date  })

    
   

        
      
    return jsonify(result)
    
    
@app.route('/')
def index():
    global result
    return result
    


if __name__ == "__main__":
    app.run(debug=True)

