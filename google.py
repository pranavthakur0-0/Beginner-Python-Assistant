import pywhatkit
from speak import speak
def googlo(query):
    query = query.replace("hey", "")
    query = query.replace("friday", "")
    query = query.replace("search", "")
    query = query.replace("on google", "")
    speak("This is what I found")
    pywhatkit.search(query)
    speak("Done sir") 