import pyttsx3
from speak import speak

def prone(query):
    eng = pyttsx3.init()
    eng.setProperty("rate", 120)
    eng.say(query)
    eng.setProperty("rate", 200)
    eng.runAndWait()
    speak("Want me to pronounce it again")
    s = takecommand()
    if 'pronounce it again' in query:
        prone(query)
        
    elif 'no' in query:
        print("")


def speed():
    assistant = pyttsx3.init()
    voices = assistant.getProperty('voices')
    assistant.setProperty('voice', voices[33].id)

def pronounce(query):  
    query = query.replace('how to pronounce ', "")  
    query = query.replace('a word ', "")
    query = query.replace('the word ', "")
    prone(query)
    speed()