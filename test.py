import os
import pyttsx3
import speech_recognition as sr
import nltk
from nltk.corpus import wordnet
import sys 
import subprocess 
from subprocess import Popen
import pyaudio
import webbrowser
import pywhatkit
import pyautogui
import wikipedia
import datetime
import time
import signal
from datetime import datetime
import pyjokes
import pronouncing
from PyDictionary import PyDictionary as diction
from googletrans import Translator
translator = Translator()

def split(word):
    return list(word)
     
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[33].id)


def listToString(s): 
    string = ","
    return (string.join(s)) 

def speak(audio):
   assistant.say(audio)
   print(f": {audio}")
   assistant.runAndWait()




engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.say("Procrastination")
engine.runAndWait()