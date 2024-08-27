import pyttsx3
from decouple import config




USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

#Set Rate
engine.setProperty('rate', 200)

#Set Volume
engine.setProperty('volume', 1.0)

#Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()

from datetime import datetime

def greet_user():
    """Greets the user according to the time."""
    
    hour = datetime.now().hour
    if(hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif(hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif(hour >= 16) and (hour < 21):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")
    

import speech_recognition as sr
from random import choice
from utils import opening_text

def take_user_input():
    """takes user input. recognizes it using speech recognition."""
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing...')
        query= r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night mam, take care!")
            else:
                speak("Have a good day mam!")
            exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = 'None'
    return query
