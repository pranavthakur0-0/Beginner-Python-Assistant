import pyttsx3
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[33].id)

def speak(audio):
   assistant.say(audio)
   print(f": {audio}")
   assistant.runAndWait()