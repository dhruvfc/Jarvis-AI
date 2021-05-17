import pyttsx3
import requests
import speech_recognition as sr
import datetime
import subprocess
import cv2
import sys
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import numpy as np
import smtplib
import PyPDF2
import operator
import urllib.request
from bs4 import BeautifulSoup 
from tkinter import *
import time
import os

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
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

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
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your email id', to, content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first", "second", "third", "fourth", "fifth"]
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

    if 'open pycharm' in query:
        speak('opening PyCharm sir, is therre anything else i can do for you?')
        print('opening...')
        subprocess.call(
            ["/usr/bin/open", "/Applications/PyCharm CE.app"]
        )

    if 'play' in query:
        youtube = query.replace('play', '')
        speak('playing... ' + youtube)
        pywhatkit.playonyt(youtube)

    if 'take screenshot' in query:
        speak('Taking screenshot')
        print('taking...')
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                             cv2.COLOR_RGB2BGR)
        cv2.imwrite("Jarvis Screenshot.png", image)

    if 'take a screenshot' in query:
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
        speak('bye Dhruv, have a great day ahead')
        sys.exit()

    elif "who is" in query:
        speak("searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
        print(results)

    elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished sir')

    elif "set alarm" in query:
        nn = int(datetime.datetime.now().hour)
        if nn == 15:
            music_dir = 'a.mp3'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open youtube' in query:
        speak('opening youtube sir, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.youtube.com/")

    elif 'open code.org' in query:
        speak('opening code.org Dhruv, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://code.org/")

    elif 'open netflix' in query:
        speak('opening netflix Dhruv, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.netflix.com/")

    elif 'open prime' in query:
        speak('opening prime Dhruv, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.primevideo.com/")

    elif 'open primevideo' in query:
        speak('opening primevideo Dhruv, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.primevideo.com/")

    elif 'open gmail' in query:
        speak('opening gmail Dhruv, is therre anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'date' in query:
        date = str(datetime.datetime.now().day)
        speak('The date is' + date)

    elif 'month' in query:
        month = str(datetime.datetime.now().month)
        speak('The month is' + month)

    elif 'year' in query:
        year = str(datetime.datetime.now().year)
        speak('The year is' + year)

    elif "open google" in query:
        speak("sir, what should i search for?")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

    elif "email test" in query:
        try:
             speak("what should i say?")
             content = takecommand().lower()
             to = "email of person you want to send"
             sendEmail(to, content)
             speak("Email has been sent to test")

        except Exception as e:
            print(e)
            speak("Sorry Dhruv, i am unable to send the email to mum")

    elif "temperature" in query or "weather" in query or "forecast" in query:
        search = "temperature in bangalore"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
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

    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")

    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    

    elif "calculate" in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("What should i calculate Dhruv?")
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        my_string=r.recognize_google(audio)
        print(my_string)
        def get_operator_fn(op):
            return{
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided by' : operator.__truediv__,
            }[op]
        def eval_binary_expr(op1, oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        speak("your awnser is: ")
        speak(eval_binary_expr(*(my_string.split())))

    elif "hello" in query or "hey" in query:
        speak("Hello sir, How may i help you?")

    elif "how are you" in query:
        speak("i am fine sir, What about you?")

    elif "good" in query or "great" in query or "fine" in query:
        speak("thats good to hear")

    elif "thank you" in query or "thanks" in query:
        speak("My pleasure sir!")

    elif "you can sleep" in query or "sleep now" in query:
        speak("okay sir, i am going to sleep, feel free to call me!")
        sys.exit()

    if 'search for' in query:
        search = query.replace('search for', '')
        speak('searching...' + search)
        pywhatkit.search(search)

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            start()
        elif "goodbye" in permission or "sleep" in permission:
            speak("Thanks for using me sir, Have a great day ahead")
            sys.exit()
