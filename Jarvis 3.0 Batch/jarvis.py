import pyttsx3
import requests
import speech_recognition as sr
import datetime
import subprocess
import cv2
import sys
import wolframalpha
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
from pyautogui import click
import numpy as np
import smtplib
import PyPDF2
import operator
import urllib.request
from bs4 import BeautifulSoup 
from tkinter import *
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import psutil
from playsound import playsound
import wave
import pyaudio
import keyboard
from keyboard import press
from keyboard import write
from PyDictionary import PyDictionary as Diction
import pywikihow
from pywikihow import search_wikihow
from time import sleep
from notifypy import notify

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180-200)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if "jarvis" in query:
            query.replace('Jarvis', '')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
    return query.lower()

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    from time import sleep
    import pyperclip

    sleep(2)
    click(x=900, y=80)
    hotkey('command', "c")
    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download("")#Saving path
    Download(Link)
    speak("Done")

def Time_Table():
    speak("Checking...")
    from Time_Table.Monday import Time

    value = Time()

    Noti = notify()

    Noti.title = "Monday's TimeTable"

    Noti.message = str(value)

    Noti.send()

    speak("Done sir is there anything else i can do for you")

def My_Location():

    op = "https://www.google.com/maps/place/Bengaluru,+Karnataka/@12.9542946,77.4908519,52904m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3bae1670c9b44e6d:0xf8dfc3e8517e4fe0!8m2!3d12.9715987!4d77.5945627"

    speak("Checking....")

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"sir , You Are currently In {state , country} .")

def passcode():
    speak("Please Enter The Correct Username and Password To Access Me")
    while True:
        username = input("What is your username :")
        pwd = input("What is the password? :")
        if username == "Guest15123" and pwd == "Guest123":# ANY USERNAME DEFAULT: Guest15123 PWD: Guest123
            speak("Access Granted!")
            break

        else:
            speak("Access Denied!")

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour > 0 and hour < 12:
        speak(f"welcome back sir, the time is {tt}, how may i help you?") #Good Morning instead of welcome back
    elif hour >= 12 and hour < 16:
        speak(f"welcome back sir, the time is {tt}, how may i help you?") #Good Afternoon instead of welcome back
    else:
        speak(f"welcome back sir, the time is {tt}, how may i help you?")  #Good Evening instead of welcome back

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR MAIL ID', 'YOUR MAIL ID PASSWORD')    #Sending E-Mail Function
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
    for i in range(len(day)):
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

def dic():
    speak("Dictionary Activated")
    speak("sir please tell me the word")
    word = takecommand()

def start():
  global result
  passcode()
  wish()
  while True:

    query = takecommand().lower()

    if "in youtube" in query:
        youtube = query.replace('in youtube', '')
        youtube = query.replace('play', '')
        speak('playing... ' + youtube)
        pywhatkit.playonyt(youtube)

    if 'open safari' in query:
        speak('opening safari sir, is there anything else i can do for you?')
        print('opening...')
        subprocess.call(
            ["/usr/bin/open", "/Applications/Safari.app"]
        )

    if 'take screenshot' in query or "take a screenshot" in query:
        speak('Taking screenshot')
        print('taking...')
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                             cv2.COLOR_RGB2BGR)
        cv2.imwrite("Jarvis Screenshot.png", image)

    if "pause" in query:
        keyboard.press('space bar')

    if "play" in query:
        keyboard.press('space bar')

    if "reload" in query or "restart" in query:
        keyboard.press('0')

    if "full screen" in query or "fullscreen" in query:
        keyboard.press('f')

    if "normal screen" in query or "normal" in query:
        keyboard.press('esc')

    if "mute sound" in query or "mute" in query:
        keyboard.press('m')

    if "forward" in query or "skip" in query:
        keyboard.press('1')

    if "backward" in query or "back" in query:
        keyboard.press('j')

    if "mode" in query:
        keyboard.press('t')

    if "alarm" in query:
        speak("Please Enter The Time !")
        time = input(": Please Enter The Time :")
        speak('your alarm is set')

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
               print('sir Get Up!!!!!!!!!!!')
               speak("sir, please wake-up")
               speak('your time is up sir get up')
               speak("sir you better be up")
               speak("Sir i am playing your song now!")
               print('sir Get Up!!!!!!!!!!!')
               os.system("afplay peaches.mp3")

            elif now > time:
                break

    if 'meaning of' in query:
        query = query.replace("what is the", "")
        query = query.replace("jarvis", "")
        query = query.replace("of", "")
        query = query.replace("meaning of", "")
        result = Diction.meaning(query)
        speak(f"The meaning of {query} is {result}")

    elif "read pdf" in query or "read book" in query:
        pdf_reader()

    elif "ip address" in query:
         ip = get('https://api.ipify.org').text
         speak(f"your IP address is {ip}")

    elif "location" in query:
        My_Location()

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
        speak('bye sir, call me if you need me')
        sys.exit()

    elif 'timer' in query or 'stopwatch' in query:
        import time
        speak("For how many minutes?")
        timing = takecommand()
        timing = timing.replace('minutes', '')
        timing = timing.replace('minute', '')
        timing = timing.replace('for', '')
        timing = float(timing)
        timing = timing * 60
        speak(f'I will remind you in {timing} seconds')
        time.sleep(timing)
        speak('Your time has been finished sir!')
        speak("I am playing your song now!")
        os.system("afplay peaches.mp3")

    elif 'stand by' in query or 'wait' in query or "weight" in query or "standby" in query or "vate" in query:
        import time
        speak("For how long?")
        j = takecommand()
        j = j.replace('minutes', '')
        j = j.replace('minute', '')
        j = j.replace('for', '')
        j = float(j)
        j = j * 60
        speak(f'ok sir i will wait for {j} seconds')
        time.sleep(j)
        print("I am Back!!!")
        speak('sir i am back, what work do we have left')

    elif 'open youtube' in query:
        speak('opening youtube sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.youtube.com/")

    elif "download video" in query:
        DownloadYouTube()

    elif "exit school" in query or "leave school" in query:
        from pyautogui import click
        from time import sleep
        speak("logging out of argus")
        sleep(1)
        click(x=23, y=472)

    elif "close" in query:
        speak('closing')
        print('closing...')
        keyboard.press_and_release('command + w')

    elif "open argus" in query or "open a r g u s" in query or "open my school" in query or "open August" in query:
        from pyautogui import click
        from time import sleep
        speak("opening argus")
        webbrowser.open("https://euro.learnindialearn.in/login")
        speak("logging in into argus")
        sleep(7)
        click(x=1093, y=469)
        sleep(1)
        click(x=965, y=560)
        sleep(3)
        click(x=677, y=394)
        pyautogui.write("ID")#ID
        sleep(1)
        click(x=665, y=468)
        pyautogui.write("PWD")#PWD
        sleep(1)
        click(x=721, y=569)
        speak("logged in")

    elif "open my classes" in query:
        from pyautogui import click
        from time import sleep
        speak("ok sir looks like you are in a hurry, please wait")
        speak("opening argus")
        webbrowser.open("https://euro.learnindialearn.in/login")
        speak("logging in into argus")
        sleep(1)
        click(x=1093, y=469)
        sleep(1)
        click(x=965, y=560)
        sleep(3)
        click(x=677, y=394)
        pyautogui.write("ID")#ID
        sleep(1)
        click(x=665, y=468)
        pyautogui.write("PWD")#PWD
        sleep(1)
        click(x=721, y=569)
        speak("logged in")
        sleep(5)
        click(x=25, y=380)
        speak("arrived at classes sir, should i start any of them?")

    elif "download" in query:
        speak("ok downloading")
        DownloadYouTube()

    elif 'open code.org' in query:
        speak('opening code.org sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://code.org/")

    elif 'open netflix' in query:
        speak('opening netflix sir, is there anything else i can do for you?')
        print('opening...')
        webbrowser.open("https://www.netflix.com/")

    elif "repeat my words" in query or "repeat after me" in query:
        speak("please go ahead sir i am listening")
        jj = takecommand()
        speak(f"you said: {jj}")

    elif "record my voice" in query or "activate voice recorder" in query or "record voice" in query:
        speak("recording your voice sir, please wait")
        import voice
        start(voice)

    elif "only chat chat bot" in query or "only chat chatbot" in query:
        import Chat_Bot
        start(Chat_Bot)

    elif "speaking chat bot" in query or "speaking chatbot" in query:
        import Speaking_chat_bot
        start(Speaking_chat_bot)

    elif "show me my calender" in query or "calender" in query:
        speak("Showing your Personalized calender sir, please wait")
        import calender
        start(calender)

    elif "record video" in query or "record my video" in query or "activate video" in query:
        speak("recording your video sir, please wait")
        import video
        start(video)

    elif "record screen" in query or "record my screen" in query or "activate screen recorder" in query:
        speak("recording your screen sir, please wait")
        import screen
        start(screen)

    elif "time table" in query or "timetable" in query:
        Time_Table()

    elif "show me my to do list" in query or "list" in query or "my todo list" in query or "show my to do list" in query:
        speak("Showing your to-do list sir")
        import To_Do
        start(To_Do)

    elif "open my browser" in query or "show me my browser" in query:
        speak("opening your personal browser sir, please wait")
        import Browser
        start(Browser)

    elif "where is" in query:
        from Google_Maps import GoogleMaps

        Place = query.replace("where is", "")
        Place = Place.replace("jarvis", "")
        Place = Place.replace("Java", "")
        Place = Place.replace("Jarvis", "")

        GoogleMaps(Place)

    elif "message" in query or "text" in query:
        from aditi import Whatsapp
        name = query.replace("message", "")
        name = name.replace("send", "")
        name = name.replace("to", "")
        name = name.replace("jarvis", "")
        name = name.replace("Jarvis", "")
        name = name.replace("Java", "")
        Name = str(name)
        speak(f"What is the message for {Name}")
        MSG = takecommand()
        Whatsapp(Name, MSG)

    elif "type" in query:
        speak("ok sir i am ready to type please tell me what to type")
        abcd = takecommand()
        write(abcd)
        speak("Done!")

    elif "write" in query:
        speak("ok sir i am ready to write please tell me what to write")
        cde = takecommand()
        write(cde)
        speak("Done!")

    elif "be awake" in query:
        import awake
        start(awake)

    elif "cut the audio call" in query or "cut the call" in query:
        from pyautogui import click
        from time import sleep
        speak("cutting the call sir")
        sleep(1)
        click(x=1390, y=72)

    elif "send a telegram" in query or "message through telegram" in query or "send telegram" in query:
        from Telegram_Chat import chat
        name = query.replace("send a telegram", "")
        name = query.replace("message", "")
        name = name.replace("send a telegram", "")
        name = name.replace("send a", "")
        name = name.replace("telegram", "")
        name = name.replace("through", "")
        name = name.replace("to", "")
        name = name.replace("jarvis", "")
        Name = str(name)
        speak(f"What is the message for {Name}")
        MSG = takecommand()
        chat(Name, MSG)

    elif "video call" in query:
        from mom import Whatsappvideomom
        name = query.replace("video call", "")
        name = name.replace("Jarvis", "")
        name = name.replace("to", "")
        name = name.replace("Java", "")
        name = name.replace("jarvis", "")
        Name = str(name)
        Whatsappvideomom(Name)

    elif "how do you like your new feature" in query:
        speak("I love It, thank you for upgrading me sir")

    elif "keep quiet" in query or "quiet" in query:
        import time
        speak("ok sir i will stop saying that!")
        speak("i will sleep for 30 seconds")
        time.sleep(30)

    elif "i know that" in query:
        speak("ok sir, great!")

    elif "telegram video call" in query or "video call through telegram" in query:
        from Telegram_video import videocall
        name = query.replace("video call", "")
        name = query.replace("to", "")
        name = name.replace("Jarvis", "")
        Name = str(name)
        videocall(Name)

    elif "audio" in query:
        from dad import Whatsappcalldad
        name = query.replace("audio call", "")
        name = name.replace("to", "")
        name = name.replace("jarvis", "")
        Name = str(name)
        Whatsappcalldad(Name)

    elif "telegram call" in query:
        from Telegram_Call import callal
        name = query.replace("telegram call", "")
        name = name.replace("jarvis", "")
        name = name.replace("to", "")
        Name = str(name)
        callal(Name)

    elif "rerun" in query or "re run" in query:
        from pyautogui import click
        from time import sleep
        speak("Re-Running my program")
        sleep(2)
        click(x=1287, y=57)

    elif "search for" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("search for", "")
        query = query.replace("search", "")
        speak("sir this is what i found on the web!")
        pywhatkit.search(query)

        try:
            result = googleScrap.summary(query, 2)
            speak(result)

        except:
            speak("no callable data")

    elif "first class" in query:
        from classes import first_class
        speak("are you logged into argus yet?")
        first_class()
        speak("connecting to class")
        speak("connected")

    elif "second class" in query:
        from classes import second_class
        speak("are you logged into argus yet?")
        second_class()
        speak("connecting to class")
        speak("connected")

    elif "third class" in query or "3rd class" in query:
        from classes import Third_class
        speak("are you logged into argus yet?")
        Third_class()
        speak("connecting to class")
        speak("connected")

    elif "fourth class" in query or "4th class" in query:
        from classes import Fourth_class
        speak("are you logged into argus yet?")
        Fourth_class()
        speak("connecting to class")
        speak("connected")

    elif "fifth class" in query or "5th class" in query:
        from classes import Fifth_class
        speak("are you logged into argus yet?")
        Fifth_class()
        speak("connecting to class")
        speak("connected")

    elif "sixth class" in query or "6th class" in query:
        from classes import Sixth_class
        speak("are you logged into argus yet?")
        Sixth_class()
        speak("connecting to class")
        speak("connected")

    elif "seventh class" in query or "7th class" in query:
        from classes import Seventh_class
        speak("are you logged into argus yet?")
        Seventh_class()
        speak("connecting to class")
        speak("connected")

    elif "how to" in query or "tell me" in query:
        speak("fetching data from web!")
        op = query.replace("jarvis","")
        max_result = 1
        how_to = search_wikihow(op, max_result)
        assert len(how_to) == 1
        how_to[0].print()
        speak(how_to[0].summary)

    elif "remember that" in query:
        rememberMsg = query.replace("remember that","")
        rememberMsg = rememberMsg.replace("jarvis","")
        speak(f"sir you told me to remind you about :" + rememberMsg)
        remember = open('data.txt','w')
        remember.write(rememberMsg)
        remember.close()

    elif "what did i ask you to remember" in query or "you remember":
        remember = open('data.txt', 'r')
        speak("sir you told me " + remember.read())

    elif 'date' in query:
        date = str(datetime.datetime.now().day)
        speak('The date is' + date)

    elif 'month' in query:
        month = str(datetime.datetime.now().month)
        speak('The month is' + month)

    elif 'year' in query:
        year = str(datetime.datetime.now().year)
        speak('The year is' + year)

    elif 'meaning of' in query:
        word = query.replace("what is the", "")
        word = word.replace("jarvis", "")
        word = word.replace("meaning of", "")
        result = Diction.meaning(word)
        speak(f"The meaning of {word} is {result}")

    elif 'synonym' in query:
        word = query.replace("what is the", "")
        word = word.replace("jarvis", "")
        word = word.replace("of")
        word = word.replace("synonym of", "")
        result = Diction.synonym(word)
        speak(f"The synonym of {word} is {result}")

    elif 'antonym' in query:
        word = query.replace("what is the", "")
        word = word.replace("jarvis", "")
        word = word.replace("of")
        word = word.replace("antonym of", "")
        result = Diction.synonym(word)
        speak(f"The antonym of {word} is {result}")

    elif "open google" in query:
        speak("sir, what should i search for?")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

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

    elif "decrease brightness" in query:
        print('Decreasing Brightness')
        pyautogui.keyDown("F1")
        pyautogui.press("F1")
        pyautogui.keyUp("F1")
        speak('your brightness had been decreased sir, is there anything else i can do for you?')

    elif "news" in query:
        speak("please wait sir, i am fetching the latest news")
        news()

    elif "help me" in query:
        speak("what do you need help with sir?")

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
                'divided by' : operator.__truediv__,
            }[op]
        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        speak("your answer is: ")
        speak(eval_binary_expr(*(my_string.split())))

    elif "hello" in query or "hey" in query:
        speak("Hello sir, How may i help you?")

    elif "thats hot" in query:
        speak("yes i know right!")

    elif "moderate" in query:
        speak("Yes sir the temperature is pretty moderate today")

    elif "thats cold" in query:
        speak("yes i know right!")

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

    elif "dictionary" in query:
        dic()

    elif "battery" in query or "power" in query:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"sir, our mac has {percentage} percent battery left!")

    elif 'synonym' in query:
        query = query.replace("what is the", "")
        query = query.replace("jarvis", "")
        query = query.replace("of")
        query = query.replace("synonym of", "")
        result = Diction.synonym(query)
        speak(f"The synonym of {query} is {result}")

    elif 'antonym' in query:
        query = query.replace("what is the", "")
        query = query.replace("jarvis", "")
        query = query.replace("of")
        query = query.replace("antonym of", "")
        query = Diction.synonym(query)
        query(f"The antonym of {query} is {result}")

    elif "thanks you can sleep now" in query:
        speak("ok sir i am going to sleep good bye!, please feel free to call me!")
        sys.exit()

    elif "open a new window" in query:
        keyboard.press_and_release('command + n')
        speak('opening a new window sir')

    elif "open a new incognito window" in query or "open a new private window" in query:
        keyboard.press_and_release('command + shift + n')
        speak('opening a new incognito window sir')

    elif "open a new tab" in query:
        keyboard.press_and_release('command + t')
        speak('opening a new tab sir')

    elif "close tab" in query or "close the tab" in query or "close the current tab" in query:
        keyboard.press_and_release('command + w')
        speak('closing the tab sir')

    elif "minimize window" in query or "minimise window" in query or "minimize the window" in query or "minimise the window" in query:
        keyboard.press_and_release('command + m')
        speak('minimizing the window sir')

    elif "hide google" in query or "hide chrome" in query:
        keyboard.press_and_release('command + h')
        speak('hiding google sir')

    elif "quit google" in query or "quit chrome" in query or "close google" in query or "close chrome" in query:
        keyboard.press_and_release('command + q')
        speak('hiding google sir')

    elif "show settings" in query or "show me the settings" in query or "show me the google settings" in query or "show me google settings" in query:
        keyboard.press_and_release('command + ,')
        speak('showing the settings sir')

    elif "show history" in query or "show me the history" in query:
        keyboard.press_and_release('command + y')
        speak('showing the history sir')

    elif "close window" in query or "close current window" in query:
        keyboard.press_and_release('command + shift + w')
        speak('closing the tab sir')

    elif "open downloads" in query or "show me my downloads" in query:
        keyboard.press_and_release('command + shift + j')
        speak('showing your downloads sir')

    elif "open the last closed tab" in query or "open the previously closed tab" in query or "open the latest closed tab" in query:
        keyboard.press_and_release('command + shift + t')
        speak('opening the last closed tab sir')

    elif "open latest page visited" in query or "open latest website" in query or "open latest page" in query:
        keyboard.press_and_release('command + [')
        speak('opening latest page visited sir')

    elif "email to test" in query or "email test" in query or "email test" in query or "email to test" in query:
        speak("sir what should i say")
        query = takecommand().lower()
        if "send a file" in query or "attach a file" in query or "file" in query:
                email = 'YOUR MAIL ID' #FILL IN YOUR MAIL ID
                password = 'YOUR MAIL ID PASSWORD'  #FILL IN YOUR MAIL ID PASSWORD
                send_to_email = 'WHO DO YOU WANNA SEND THE MAIL TO'#
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2 
                speak("sir please enter the correct path of the file into the shell")
                
                file_location = input("please enter the path here: ")# take wherabouts and add /filename

                speak("sir please wait,i am sending email now")

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
                speak("email has been sent to mum, do you have any other work")

        else:
                email = 'YOUR MAIL ID'  #YOUR MAIL ID
                password = 'MAIL ID PASSWORD'  #MAIL ID PASSWORD
                send_to_email = 'WHO YOU WANT TO SEND THE MAIL TO'  #THE PERSON!
                message = query  

                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()  
                server.login(email, password)  
                server.sendmail(email, send_to_email,
                                message)  
                server.quit()  
                speak("email has been sent to test, do you have any other work?")

start()
