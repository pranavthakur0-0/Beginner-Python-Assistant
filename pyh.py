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
import googletrans
from googletrans import *
import wikipedia
import datetime

assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[33].id)

def speak(audio):
   assistant.say(audio)
   print(f": {audio}")
   assistant.runAndWait()

with open('data.txt') as f:
    lines = f.read()
    speak(lines)