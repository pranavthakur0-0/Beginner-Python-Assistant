import speech_recognition as sr
from speak import speak
import googletrans
from googletrans import *

def takelanguage():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisiting... ")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio)
            print(query)

        except Exception as Error:
            return "none"

        return query.lower()

def translator(query):
    speak('Say, what you want to translate')
    while(True):
       query = takelanguage()
       query = str(query)
       if 'none' in query:
           continue
       if 'exit translator' in query:
           break
       else:
           query = str(query)
           translate = googletrans.Translator()
           translate = translate.translate(query , dest = 'en')
           print(translate.text)
           speak(translate.text)