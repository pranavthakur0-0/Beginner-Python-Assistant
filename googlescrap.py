import wikipedia as googlescrap
import pywhatkit
from speak import speak

def googli(query):
    query = query.replace('friday ',"")
    query = query.replace('search',"")
    query = query.replace('what is the ',"")
    query = query.replace('what is ',"")
    speak("Searching over the internet")
    pywhatkit.search(query)

    try:

        result = googlescrap.summary(query,2)
        speak(result)
             
    except:
        speak("Sorry sir!, no useful content was found")


a = 'ironman'
googli(a)