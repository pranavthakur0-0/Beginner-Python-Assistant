from wikipedia import wikipedia
from speak import speak
def wikip(query):    
    speak("searching wilipedia....")
    query = query.replace('search', "")
    query = query.replace('on wikipedia', "")
    print(query)
    wiki = wikipedia.summary(query,2)
    speak('According to wikipedia :'+ wiki)