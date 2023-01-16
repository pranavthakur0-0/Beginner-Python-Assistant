import pyttsx3
import speech_recognition as sr
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisiting... ")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio,language="en-in")
            print(query)

        except Exception as Error:
            return "none"

        return query.lower()