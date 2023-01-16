import webbrowser
from speak import speak
def youtu(query):
    query = query.replace("hey", "")
    query = query.replace("friday", "")
    query = query.replace("search", "")
    query = query.replace("on youtube", "")
    query = query.replace("searchonyoutube", "")
    speak("This is what I found")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)
    speak("Done sir")