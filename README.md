# Facial-recognition-enabled-Voice-Assistant
This is a virtual assistant for our laptops with in built facial
recognition for authentication of user and interactive user interface.
By the click of a button, one can give instructions to his/her computer and
have the system perform easy tasks with great accuracy and efficiency.
This assistant listens for the user’s message, breaks it down, evaluates it
and offers a meaningful response in return. Not only it increases the productivity, but speech
recognition software nowadays capture speech much faster than a
human’s average typing speed.

# UML DIAGRAMS

⦁	CLASS DIAGRAM
![Preview](https://github.com/param629/Facial-recognition-enabled-Voice-Assistant/blob/main/Param/classdiagram.png)
Class diagram is a static diagram. It represents the static view of an application. Class diagram is not only used for visualizing, describing, and documenting different aspects of a system but also for constructing executable code of the software application.
Class diagram describes the attributes and operations of a class and also the constraints imposed on the system. The class diagrams are widely used in the modeling of objectoriented systems because they are the only UML diagrams, which can be mapped directly with object-oriented languages.



 

⦁	ACTIVITY DIAGRAM
![Preview](https://github.com/param629/Facial-recognition-enabled-Voice-Assistant/blob/main/Param/activitydiagram.jpg)
Activity diagram is another important diagram in UML to describe the dynamic aspects of the system.
Activity diagram is basically a flowchart to represent the flow from one activity to another activity. The activity can be described as an operation of the system.
The control flow is drawn from one operation to another. This flow can be sequential, branched, or concurrent. Activity diagrams deal with all type of flow control by using different elements such as fork, join, etc




 





⦁	USE CASE DIAGRAM

![Preview](https://github.com/param629/Facial-recognition-enabled-Voice-Assistant/blob/main/Param/usecasediagram.jpg)


The purpose of use case diagram is to capture the dynamic aspect of a system. Use case diagrams are used to gather the requirements of a system including internal and external influences. These requirements are mostly design requirements. Hence, when a system is analysed to gather its functionalities, use cases are prepared and actors are identified.
When the initial task is complete, use case diagrams are modelled to present the outside view.


 

# Methodology
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

# APPLICATIONS

● It can be used to play music
● It can do Wikipedia searches
● It can open websites for the user
● It can open various software on the system
● It can send WhatsApp Messages
● It is for our personal use and takes commands only from the user
● It can create a to-do list for our daily goals
● It can tell jokes and tell the time
● It can tell the weather of the city specified
