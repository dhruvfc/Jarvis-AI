#Jarvis Version 2.0
#To activate Jarvis you must say "Jarvis Wake up"
#Please read all instruction before use!

import pyttsx3
import time
import os
import requests
import speech_recognition as sr
import datetime
import subprocess
import cv2
import sys
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import numpy as np
import smtplib
import PyPDF2
import operator
import urllib.request
from requests import get
from bs4 import BeautifulSoup 
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180-200)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour < 12:
        speak("Good Morning sir, How may i help you?")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir, How may i help you?")
    else:
        speak("Good Evening sir, How may i help you?")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ID', 'YOUR E-MAIL ID PASSWORD')#please write the info here!
    server.sendmail('your email id', to, content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=91a890b41e5c473c814dcb5d88bf4939'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('book.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book are{pages} ")
    speak("sir please tell me the number of pages i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def start():
  wish()
  while True:

    query = takecommand().lower()

    if 'open google' in query:
        speak('opening google sir, is there anything else i can do for you?')
        print('opening...')
        subprocess.call(
            ["/usr/bin/open", "/Applications/Google Chrome.app"]
        )

    elif "close google" in query:
        print("closing google...")
        pyautogui.keyDown("command")
        pyautogui.press("q")
        pyautogui.keyUp("command")
        speak('closing google sir, do you need anything else?')

    if 'play' in query:
        youtube = query.replace('play', '')
        speak('playing... ' + youtube)
        pywhatkit.playonyt(youtube)

    if 'screenshot' in query:
        speak('Taking screenshot')
        print('taking...')
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                             cv2.COLOR_RGB2BGR)
        cv2.imwrite("Jarvis Screenshot.png", image)

    elif "read pdf" in query:
        pdf_reader()

    elif "ip address" in query:
         ip = get('https://api.ipify.org').text
         speak(f"your IP address is {ip}")

    elif 'bye jarvis' in query:
        print('shutting down...')
        speak('bye sir, have a great day ahead')
        sys.exit()

    elif "who is" in query:
        speak("searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
        print(results)

    elif "no thanks" in query:
        speak('bye sir, call me if you need me!')
        sys.exit()

    elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished sir, please wake up')
            speak("I am Playing your song now")
            os.system("afplay peaches.mp3")

    elif 'open youtube' in query:
        speak('opening youtube sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.youtube.com/")

    elif 'open netflix' in query:
        speak('opening netflix sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.netflix.com/")

    elif 'show me my mail' in query or "open gmail" in query or "open Gmail" in query or "show me my inbox":
        speak('opening mail sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'what is the date' in query:
        date = str(datetime.datetime.now().day)
        speak('The date is' + date)

    elif 'what is the month' in query:
        month = str(datetime.datetime.now().month)
        speak('The month is' + month)

    elif 'what is the year' in query:
        year = str(datetime.datetime.now().year)
        speak('The year is' + year)

    elif "open google" in query:
        speak("sir, what should i search for?")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

    elif "temperature" in query or "weather" in query or "forecast" in query:
        search = "temperature in bangalore"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current {search} is {temp}")

    elif "switch tab" in query:
        print("switching tab...")
        pyautogui.keyDown("command")
        pyautogui.press("tab")
        pyautogui.keyUp("command")
        speak('Switching tab sir, do you need anything else?')

    elif "news" in query:
        speak("please wait sir, i am fetching the latest news")
        news()

    elif "calculate" in query or "can you calculate" in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("What should i calculate sir?")
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        my_string = r.recognize_google(audio)
        print(my_string)
        def get_operator_fn(op):
            return{
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                'divided by': operator.__truediv__,
            }[op]
        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        speak("your answer is: ")
        speak(eval_binary_expr(*(my_string.split())))

    elif "hello" in query or "hey" in query:
        speak("Hello sir, How may i help you?")

    elif "how are you" in query:
        speak("i am fine sir, What about you?")

    elif "good" in query or "great" in query or "fine" in query:
        speak("thats good to hear")

    elif "thank you" in query or "thanks" in query:
        speak("My pleasure sir!")

    elif "shutdown" in query:
       speak("ok sir, i am shutting down, feel free to call me")
       print("shutting down...")
       sys.exit()

    elif "sleep" in query:
        speak("ok sir, i am going to sleep, feel free to call me!")
        print("sleeping.zzzzzz")
        sys.exit()

    if 'search for' in query:
        search = query.replace('search for', '')
        speak('searching...' + search)
        pywhatkit.search(search)

    elif "email to test" in query or "email test" in query:

        speak("sir what should i say")
        query = takecommand().lower()
        if "send a file" in query:
                email = 'YOUR EMAIL ID' #FILL IT
                password = 'YOUR EMAIL-ID PASSWORD'  #FILL IT
                send_to_email = 'WHO YOU WANT TO SEND THE MAIL TO' #WHO DO YOU WANT TO SEND THE MAIL TO?
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2 
                speak("sir please enter the correct path of the file into the shell")
                
                file_location = input("please enter the path here: ")# take wherabouts and add /filename

                speak("sir please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

               
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to test, do you have any other work")

        else:
                email = 'YOUR MAIL ID'  #FILL IN YOUR MAIL ID
                password = 'MAIL ID PASSWORD' #FILL IN YUOR MAIL-ID PASSWORD
                send_to_email = 'WHO YOU WANNA SEND THIS MAIL TO' #FILL IT IN
                message = query  

                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()  
                server.login(email, password)  
                server.sendmail(email, send_to_email,
                                message)  
                server.quit()  
                speak("email has been sent to test, do you have any other work?")

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            start()
