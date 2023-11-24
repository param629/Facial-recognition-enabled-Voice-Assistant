# Facial-recognition-enabled-Voice-Assistant
1. VOICE ASSISTANT
a. The first and foremost thing for a voice assistant is that it should be
able to speak. For this we also need a python library that converts text
to speech. We initialize the voice engine of our system and get the
properties of the inbuilt voices in our system
b. Now, we made a wish me function that greets the user according to the
time of the PC.
c. Next most important part of thing for our assistant is that it should take
command with the help of the microphone of the user’s system. Our A.I
system returns string output by taking microphone input from the user.
d. After these basic functionalities came the main coding logic for the
assistant. It included the logic behind tasks which the assistant was
about to perform. These tasks were:
i. Do Wikipedia searches using the Wikipedia module
ii. Open YouTube site using webbrowser
iii. To open various software of our system using os module
iv. To send WhatsApp messages
v. To tell the weather of any city

2. FACIAL RECOGNITION

a. Firstly, we load the image file of the user to train the model, encode
that image and store the encodings.
b. Then we start with the actual process of face recognition by opening
the camera of the PC.
c. The camera captures real time image of the user and creates its own
encoding for that image.
d. After this, the two encodings are compared with the by finding
Euclidean distance between the encodings.
● If there are a number of people in the camera, it calculates
Euclidean distances with all the encodings and finds the one with
the least value of the distance.
e. If the encodings match, the user is authenticated and the page for
taking commands is loaded. Else, an error page is shown by the
system.

3. WEB UI
a. Firstly, distinct html pages with embedded CSS are created to display
the various parts of the system
b. Then these pages are routed to different URLs so that connection
between the pages and flow of the system can be established.
c. At last, these pages are mapped with specific functions and definition
of what will happen when a certain button on a specific page is clicked.
