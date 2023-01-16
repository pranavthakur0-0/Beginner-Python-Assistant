from speak import speak
from datetime import datetime
from takecommand import takecommand
import re
from playsound import playsound ##playsound only works with wav files 

def alarm():
    speak("Tell the time please")
    time = takecommand()
    time = time.replace('p.m.', "PM")
    time = time.replace('a.m.', "AM")
    print(time, "your time")
    now = (datetime.today().strftime("%I:%M %p"))
    print(now, "now time")
    time1 = str(time)
    whil(time1)

def whil(time1):

    while(True):
        print('ss')
        now1 = (datetime.today().strftime("%I:%M %p"))
        now1 = re.sub('0',"", now ,1)
        if(now1 == time1):
            speak("Time to wake up sir!")
            playsound("Ironman.wav")
            break
        
        elif now1>time1:
            continue