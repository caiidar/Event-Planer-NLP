# Event-Me-NLP
# What is EventMe?
The first idea for our application was given through partyholic. Our Main idea was to create an application to help one organising and not forgetting an event seen on e.g. an advertisement. Basically the application shall use a new picture taken or from the gallery and analyse any text on it. We are specifically looking for dates and a related location for the event.
In our research we found several many calendar or event planning applications. None of them were for event management in that way we designed our to help manage and organize them e.g. connecting the app with one's Google calendar and instantly adding the event. The way our application sets events and finds the information is seemingly the only one at the moment. Thus it appears we found a gap in the market. After talking to one another and figuring out how we wanted the application to work we arranged us with what was to do. So we started EventMe.
# Backend:
This is the backend of EventMe.
We used Flask as a way to create a simple web application, as it does not require particular tools or libraries.  
We deployed that application to Heroku which is a cloud platform using containers to run our application on a virtual environment. We tested different iterations of the application using separate containers, pushing our code directly from GitHub. 
The most important task of our backend is the image processing for this we used Google Cloud Vision. It is a powerful and reliable API that analyses images via deep learning. Vast quantities of training data provided from Google makes it better than most similar APIs
# Frontend:
This is the frontend of EventMe. Here you are going to get the .apk file directly above to install our app. We used Android Studio and recommend opening with Android Studio. Android Studio has a very own way managing files so its shows the best structure possible. Please use the FrontEnd branch to download the project. The layout file show how we structured our app and the java files hold all of our functionallity.
Preview:

![Bildschirmfoto 2021-08-19 um 20 22 24](https://user-images.githubusercontent.com/83280365/130123522-2dd86204-306c-4336-9876-62f1a99927a6.png)
![Bildschirmfoto 2021-08-19 um 20 29 31](https://user-images.githubusercontent.com/83280365/130124532-2467fde3-31bb-496a-8d1e-a6e0c3cf660b.png)
![Bildschirmfoto 2021-08-19 um 20 29 56](https://user-images.githubusercontent.com/83280365/130124536-84fc237c-3b26-4c13-b2c3-d0db5ed65839.png)



# How to install the frontend:
1. Download our .apk file
2. Install the .apk
3. Open the app
4. Agree to all permissions (camera, gallery, calender)
5. Snap a picture of an event or open the gallery
6. Confirm using the picture
7. Wait...
8. Now you can add it to your calender!
