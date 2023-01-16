import webbrowser
from speak import speak
def webi(query):
    query = query.replace("hey", "")
    query = query.replace("search", "")
    query = query.replace("for", "")
    query = query.replace("friday", "")
    query = query.replace("openwebsite", "")
    query = query.replace("open", "")
    query = query.replace("website", "")
    name = query.replace(" ", "")
    speak("Ok sir, Launching")
    web1 = 'https://www.'+name +'.com'
    print(web1)
    webbrowser.open(web1)
    speak("website is here")