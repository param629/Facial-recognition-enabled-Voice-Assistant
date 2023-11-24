from lib2to3.pgen2.token import MINUS
from msilib.schema import Error
from urllib import response
from flask import Flask,render_template,redirect,request,url_for,Response
import warnings
warnings.filterwarnings('ignore')

import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import datetime
import pywhatkit as pwt
import pyjokes
import requests, json, sys
from tkinter import *
from PIL import ImageTk,Image
import os
import cv2
import face_recognition as fr
import numpy as np

app = Flask("__name__")

def facial_recognition():
    condition = False
    video_capture = cv2.VideoCapture(0)

    bruno_image = fr.load_image_file("Param/param.jpg")
    bruno_face_encoding = fr.face_encodings(bruno_image)[0]

    known_face_encondings = [bruno_face_encoding]
    known_face_names = ["PARAMPREET"]

    while True: 
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_face_encondings, face_encoding)

            name = "Wrong"

            face_distances = fr.face_distance(known_face_encondings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                condition = True
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Webcam_facerecognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return condition

def speak(audio):

    engine = pyttsx3.init('sapi5')

    voices= engine.getProperty('voices') 

    engine.setProperty('voice',voices[0].id)

    engine.say(audio) 
    engine.runAndWait()


def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("How May I help you")

def weather(city):
    api_key = 'f0264ea588cbcba370525e5a66f54cd7'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" +city_name

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":

        y=x["main"]
        current_temperature = y["temp"]

        return str(current_temperature)


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 

    except Exception as e:
        print("Say that again please...")  
    return query
    
def run_alexa():
    wishme()
    query = takeCommand().lower() 

        
    if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")
        
    elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")    
            speak("Mam, the time is" + strTime)
            print("Mam, the time is " + strTime)

    elif 'open code' in query:
            codePath = "C:\\Users\\NITJ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
    elif 'open snipping tool' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool.lnk"
            os.startfile(codePath)

    elif 'play' in query:
            song = query.replace("play","")
            speak("Playing" + song)
            pwt.playonyt(song)

    elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

    elif 'weather' in query:
            speak("Please tell the name of the city")
            city = takeCommand().lower()
            weather_api = weather(city)
            print(weather_api + " Kelvin")
            speak(weather_api + "Kelvin")
        
    elif 'send message' in query:
            speak("Please tell the name of the recipient")
            name = takeCommand().lower()
            speak("Please tell the message you want to send")
            message = takeCommand().lower()
            if (name == "kushal"):
                contact = "+919627762983"
            elif(name=="anchal"):
                contact = "+919810813227"
            elif(name=="salim"):
                contact = "+919675574849"
            elif(name=="dilbag sir"):
                contact = "+919759950380"
            elif(name=="parampreet"):
                contact = "+919876909250"
            
            time = datetime.datetime.now()
            time_to_send = time + datetime.timedelta(minutes=4)
            one = time_to_send.hour
            two = time_to_send.minute
            
            pwt.sendwhatmsg(contact,message,one,two)

    elif 'open to do list' in query:
            speak("Opening to do list")
            codePath = "C:\\Param\\MajorProject\\ToDoList.txt"
            os.startfile(codePath)
            task = takeCommand().lower()
            if 'add' in task:
                task = task.replace("add","")
                with open("C:\\Param\\MajorProject\\ToDoList.txt","a") as f:
                    try:
                      x = f.write(task + "\n")
                      f.close()
                      print("Adding task complete")
                      speak("Adding task complete")

                    except Error as er:
                        print(er)
            
            if 'delete' in task:
                task = task.replace("delete","")
                with open("C:\\Param\\MajorProject\\ToDoList.txt", "r") as f:
                    lines = f.readlines()
                    f.close()
                with open("C:\\Param\\MajorProject\\ToDoList.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != task:
                            f.write(line)
                    f.close()
                    print("Deleting task complete")
                    speak("Deleting task complete")
                    


@app.route('/')
def hello():
    return render_template("hello.html")

@app.route("/home")
def home():
    return redirect('/')

@app.route("/alexa")
def project():
    return render_template("alexa.html")

@app.route("/stop")
def stop():
    return render_template("stop.html")

@app.route('/',methods=['POST', 'GET'])
def face_recognition():
    condition = facial_recognition()
    if(condition == True):
        return redirect("/alexa")
    else:
        return redirect("/stop")

@app.route("/alexa",methods=['POST', 'GET'])
def alexa():
    run_alexa()
    return render_template("alexa.html")

if __name__ =="__main__":
    app.run(debug=True)

