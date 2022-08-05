from tkinter import *
import tkinter as tk
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import winshell
import requests
import wolframalpha
import pywhatkit as pwt
import smtplib
import time
import pyautogui
import calendar
import math
import winsound
from pygame import mixer
import tkinter.messagebox as message



a = {'me':'email id 1','Sam':'email id 2','shivam':'email id 3','vishal':'email id 4'}                 #replace with valid name and email id
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = tk.Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password')            #replace with master/sender email id and app-password generated from email provider
    server.sendmail('email id', to, content)
    server.close()

def whatsapp():
    query = takeCommand().lower()
    if 'y' in query:
        pyautogui.moveTo(250,1200) 
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(100,140)   
        pyautogui.click() 
        speak('To whom you want to send message,.....just write the name in search bar in 10 seconds')
        time.sleep(10)
        pyautogui.moveTo(120,300)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(800,990)
        pyautogui.click()
        speak('Say the message,....or if you want to send anything else,...say send document, or say send emoji')
        query = takeCommand()
        if ('sent' in query or 'send' in query) and 'document' in query:
            pyautogui.moveTo(660,990)   
            pyautogui.click() 
            time.sleep(1)
            pyautogui.moveTo(660,680) #660,740
            pyautogui.click()
            speak('please select the document within 10 seconds')
            time.sleep(12)
            speak('Should I send this document?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the document......')
                pyautogui.press('enter')
                #
                time.sleep(2)
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('document' in query or 'message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        elif ('sent' in query or 'send' in query) and 'emoji' in query:
            pyautogui.moveTo(620,990)  
            pyautogui.click() 
            pyautogui.moveTo(670,990)
            pyautogui.click()
            pyautogui.moveTo(650,580) 
            pyautogui.click()
            speak('please select the emoji within 10 seconds')
            time.sleep(11)
            speak('Should I send this emoji?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('Sending the emoji......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doublClick(x=800, y=990)
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        else:
            pyautogui.write(f'{query}')
            speak('Should I send this message?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the message......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)               
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
    else:
        speak('ok')   

def detect_face():
    cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)
        speak("detecting face")
        print("Detecting face.....")
        time.sleep(10)      
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    

def brightness():
    try:
        query = takeCommand().lower()
        if '25' in query:
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1610,960)
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '50' in query:
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1684,960)   
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '75' in query:
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1758,960)   
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '100' in query or 'full' in query:
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1835,960)   
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        else: 
            speak('Please select 25, 50, 75 or 100....... Say again.')
            brightness()
    except exception as e:
        #print(e)
        speak('Something went wrong')


def close_window():
    try: 
        if 'y' in query:
            pyautogui.moveTo(1885,10)
            pyautogui.click()
        else:
            speak('ok')
            pyautogui.moveTo(1000,500)
    except exception as e:
        #print(e)
        speak('error')
        

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        var.set("Hello ! Good Morning Sir")
        window.update()
        speak("Hello ! Good Morning Sir!")
    elif 12 <= hour <= 18:
        var.set("Hello ! Good Afternoon Sir!")
        window.update()
        speak("Hello ! Good Afternoon Sir!")
    else:
        var.set("Hello ! Good Evening Sir")
        window.update()
        speak("Hello ! Good Evening Sir!")
    speak("Myself SAIRA! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        speak("Pardon me, please say that again")
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='green')
    wishme()
    while True:
        btn1.configure(bg='dark blue')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            speak("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            break


#general conversation

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif ('old are you' in query) or ('version' in query):
            var.set("Version 0.1.1 ")
            window.update()
            speak("I am a newbie sir ! Version 0.1.1")

        elif 'your name' in query:
            var.set("Myself SAIRA")
            window.update()
            speak("Myself SAIRA")

        elif 'who made you' in query:
            var.set("My Creator is team 8")
            window.update()
            speak("My Creator is team 8")

        elif ('sleep' in query) or ('close program' in query) or ( 'quit' in query) or ( 'exit' in query) or ( 'stop' in query) or ( 'shutdown' in query) or ( 'close' in query) or ( 'bye' in query):
            var.set('Sleeping...............')
            window.update()
            speak("OK bye Sir!! time to sleep have a good day")
            quit()
#searching on google and playing piano
        
                
        elif 'piano' in query:
            speak('Yes sir, I can play piano.')           
            winsound.Beep(200,500)            
            winsound.Beep(250,500)           
            winsound.Beep(300,500)            
            winsound.Beep(350,500)            
            winsound.Beep(400,500)            
            winsound.Beep(450,500)           
            winsound.Beep(500,500)
            winsound.Beep(550,500)
                        
            time.sleep(6)
            
        elif 'play' in query and 'instru' in query:
            speak('Yes sir, I can play piano.')           
            winsound.Beep(200,500)            
            winsound.Beep(250,500)           
            winsound.Beep(300,500)            
            winsound.Beep(350,500)            
            winsound.Beep(400,500)            
            winsound.Beep(450,500)           
            winsound.Beep(500,500)
            winsound.Beep(550,500)
                        
            time.sleep(6)
            
#System date ,time and alarm
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I %M %S %p")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'day after tomorrow' in query or 'date after tomorrow' in query:
            td = datetime.date.today() + datetime.timedelta(days=2)
            print(td)
            speak(td)
        elif 'day before today' in query or 'date before today' in query or 'yesterday' in query or 'previous day' in query:
            td = datetime.date.today() + datetime.timedelta(days= -1)
            print(td)
            speak(td)
        elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
            td = datetime.date.today() + datetime.timedelta(days=1)
            print(td)
            speak(td)
        elif 'month' in query or ('current' in query and 'month' in query):
            current_date = date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            speak(f'Current month is {month}')
        elif 'date' in query or ('today' in query and 'date' in query) or 'what is today' in query or ('current' in query and 'date' in query):
            current_date = date.today()           
            print(f"Today's date is {current_date}")
            speak(f'Todays date is {current_date}')
            
        elif 'year' in query or ('current' in query and 'year' in query):
            current_date = date.today()
            m = current_date.year
            print(f'Current year is {m}')
            speak(f'Current year is {m}')
        
#open system folders and softwares
#still i have to provide path for movies,software,series,python



        elif 'code' in query:
            var.set("Opening V S Code")
            window.update()
            speak("Opening V S Code")
            os.startfile("C:\\Users\\samir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'open github' in query:
            var.set('opening github')
            window.update()
            speak('opening github')
            webbrowser.open('https://github.com/MaiSamirHu')

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")

        
        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open sublime' in query:
            var.set('Opening Sublime')
            window.update()
            speak('opening Sublime')
            os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")

        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("C:\\Users\\samir\\anaconda3\\Scripts\\anaconda-navigator-script.py")

        elif 'news' in query:
            var.set('Opening news')
            window.update()
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
            
#playing games

        elif 'play' in query and 'game' in query: 
            speak('I have 2 games mario and dyno games for single player. Which one of these 2 games you want to play?')
            query = takeCommand().lower()
            
            
            if 'mar' in query or 'mer' in query or 'my' in query:
                
                webbrowser.open('https://chromedino.com/mario/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)
                
            elif 'di' in query or 'dy' in query:                
                webbrowser.open('https://chromedino.com/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)                    
            else:
                speak('ok sir')

#email sending and whatsapp

        elif 'email to' in query:
            try:
                query = query.replace("email to", "")
                query = query.replace(" ", "")
                print(query)
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a[query]
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')


        elif 'whatsapp' in query:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
            speak('Do you want to send message to anyone through whatsapp, .....please answer in yes or no')
            whatsapp()
            

# searching on internet
        elif 'wh' in query or 'how' in query:
            url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU" 
            webbrowser.open_new(url)
            time.sleep(2)
            speak('Here is your answer')
            time.sleep(5)
#random module 


        elif ('play music' in query) or ('music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C://Users//samir//OneDrive//Desktop//SAIRA-Desktop-Assistant-main//music'
            songs = os.listdir(music_dir)
            n = random.randint(0, 0)
            os.startfile(os.path.join(music_dir, songs[n]))

#Wikipedia module

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

#empty recycle bin

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

# detect face
        elif 'detect face' in query:
            speak("detecting face , hold on for seconds")
            detect_face()
#Wolframe Alpha API
#working for calculation 
        elif "calculate" in query:  
            app_id = ""
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("")
            res = client.query(query)
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
                speak('No results found')

#closing windows
        elif 'close' in query and ('click' in query or 'window' in query):
            pyautogui.moveTo(1885,10)
            speak('Should I close this window?')
            query = takeCommand().lower()
            close_window()

#Google Map access

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")

#Open weather API
# working on weather
        elif 'weather' in query:            
            webbrowser.open('https://www.yahoo.com/news/weather')
            time.sleep(3)
            speak('Click on, change location, and enter the city , whose whether conditions you want to know.')
            time.sleep(10)
        # elif 'weather' in query:
        #     api_key = ""
        #     base_url = "http://api.openweathermap.org/data/2.5/weather?"
        #     speak("what is the city name")
        #     city_name = takeCommand()
        #     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        #     response = requests.get(complete_url)
        #     x = response.json()
        #     if x["cod"] != "404":
        #         y = x["main"]
        #         current_temperature = y["temp"]
        #         current_humidiy = y["humidity"]
        #         z = x["weather"]
        #         weather_description = z[0]["description"]
        #         speak(" Temperature in kelvin unit is " +
        #               str(current_temperature) +
        #               "\n humidity in percentage is " +
        #               str(current_humidiy) +
        #               "\n description  " +
        #               str(weather_description))
        #         print(" Temperature in kelvin unit = " +
        #               str(current_temperature) +
        #               "\n humidity (in percentage) = " +
        #               str(current_humidiy) +
        #               "\n description = " +
        #               str(weather_description))
#dictionary

        elif 'dictionary' in query:
            webbrowser.open('https://www.dictionary.com')
            time.sleep(3)
            speak('Enter the word, in the search bar of the dictionary, whose defination or synonyms you want to know')
            time.sleep(15)
#Open anything on youtube

        elif 'on youtube' in query:
            song = query.replace('play','')
            var.set('Playing on Youtube')
            speak('playing'+song)
            pwt.playonyt(song)

#open camera and screenshot, video recording ,taking image 

        elif ('click photo'  in query or 'open camera' in query):
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
                stream.release()

        elif 'screenshot' in query:
            speak('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
            time.sleep(4)
            speak('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('my_screenshot.png') 
            speak('The screenshot is saved as my_screenshot.png')

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()

#brightness and volume, start bar and search in it and open file,notification

        elif ('increase' in query or 'decrease' in query or 'change' in query or 'minimize' in query or 'maximize' in query) and 'brightness' in query:
            speak('At what percent should I kept the brightness, 25, 50, 75 or 100?')
            brightness()

        elif 'click' in query and 'start' in query:
            pyautogui.moveTo(10,1200)    
            pyautogui.click()
        elif ('open' in query or 'click' in query) and 'calendar' in query:
            pyautogui.moveTo(1800,1200)   
            pyautogui.click() 
        elif 'minimise' in query and 'screen' in query:
            pyautogui.moveTo(1770,0)   
            pyautogui.click()
        elif 'increase' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumeup') 
        elif 'decrease' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumedown')
        elif 'capslock' in query or ('caps' in query and 'lock' in query):
            pyautogui.press('capslock')
        elif 'mute' in query:
            pyautogui.press('volumemute')
        elif 'search' in query and ('bottom' in query or 'pc' in query or 'laptop' in query or 'app' in query):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            speak('What do you want to search?')
            query = takeCommand().lower() 
            pyautogui.write(f'{query}')
            pyautogui.press('enter')

        elif 'night light' in query and ('on' in query or 'off' in query or 'close' in query):
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1840,620)
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
        
        elif 'notification' in query and ('show' in query or 'click' in query or 'open' in query or 'close' in query or 'on' in query or 'off' in query or 'icon' in query or 'pc' in query or 'laptop' in query):
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()

#opening various inbuild apps

        elif 'open' in query:
            if 'gallery' in query or 'photo' in query or 'image' in query or 'pic' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('photo')
                pyautogui.press('enter')
            
            elif 'word' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('word')
                pyautogui.press('enter')
            elif ('power' in query and 'point' in query) or 'presntation' in query or 'ppt' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('ppt')
                pyautogui.press('enter')
            elif 'file' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('file')
                pyautogui.press('enter')
            elif 'edge' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('microsoft edge')
                pyautogui.press('enter')
            
            elif 'spyder' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('spyder')
                pyautogui.press('enter')
            elif 'snip' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('snip')
                pyautogui.press('enter')
            
            elif 'this pc' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('this pc')
                pyautogui.press('enter')
            
            
            
            
            elif ('vs' in query or 'visual studio' in query) and 'code' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('visual studio code')
                pyautogui.press('enter')
            
#User Interface


def update(ind):
    frame = frames[ind % 10]
    ind += 1
    label.configure(image=frame)
    window.after(10, update, ind)


label2 = Label(window, textvariable=var1, bg='#730cfa')
label2.config(font=("Fixedsys", 30))
var1.set('YOU SAID:')
label2.pack(pady=10)

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Fixedsys", 20))
var.set('Welcome')
label1.pack()

# noinspection PyRedundantParentheses
frames = [PhotoImage(file='SAIRA.gif', format='gif -index %i'% (i)) for i in range(10)]
window.title('SAIRA ')
window.iconbitmap(r'msit.ico')

label = Label(window, width=500, height=150)
label.pack(pady=135) 
window.after(0, update, 0)


def mode1():
    window.configure(bg='black')


def mode2():
    window.configure(bg='#f0f0f0')


btn0 = Button(text='SAY HI', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='START', width=20, command=play, bg='DARK BLUE')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='QUIT', width=20, command=window.destroy, bg='RED')
btn2.config(font=("Courier", 12))
btn2.pack()
btn3 = Button(window, text='DARK MODE', width=20, command=mode1, bg='Black', fg='White')
btn3.config(font=("Courier", 12))
btn3.pack()
btn4 = Button(window, text='LIGHT MODE', width=20, command=mode2, fg='Black', bg='WHITE')
btn4.config(font=("Courier", 12))
btn4.pack()

window.mainloop()
