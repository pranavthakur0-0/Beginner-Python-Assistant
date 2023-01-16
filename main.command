from takecommand import takecommand
from temperaturefile import temp
from remember import rememberfunciton
from translator import translator
from speak import speak
from rememberit import rememberit
from pronounce import pronounce
from spell import spell
from screenshot import screen
import pyaudio
from youtube import youtu
from website import webi
from wikipedia1 import wikip
from Music import music
import pyjokes
from close import closeapp
from open1 import app







##this works for mac but simple version of this won't work on mac
##https://tutor.python.narkive.com/nmyn7Fqh/why-is-startfile-unavailable-on-my-mac

     

def taskexe():

    while True:

        query = takecommand()

        if 'hello' in query:
            speak("Hello sir, I am friday")
            speak("Your Personal AI assistant!")
            speak("How may i help you ")

        elif 'are you up' in query:
            speak("for you sir always")

        elif 'gotta go' in query:
            speak("ok sir")
            break

        elif 'youtube' in query:
            youtu(query)


        elif 'google' in query:
            googlo(query)

##always write the speech containing varible in single quotes then it will work
        elif 'website' in query:
            webi(query)

        elif 'play music' in query:
            music()

        elif 'wikipedia' in query:
            wikip(query)

        elif 'whatsapp' in query:
            whatsapp(query)

        elif 'screenshot' in query:
            screen()

        elif 'open application' in query:
            app(query)

        elif 'close application' in query:
            closeapp(query)

        elif 'pause video' in query:
            pyautogui.press('space')
        
        elif 'play video' in query:
            pyautogui.press('space')
            
        elif 'restart video' in query:
           pyautogui.hotkey('0')
            
        elif 'mute video' in query:
            pyautogui.hotkey('mute')

        elif 'skip video' in query:
            pyautogui.hotkey('1')

        elif 'back' in query:
            pyautogui.hotkey('j')

        elif 'full screen' in query:
            pyautogui.hotkey('f')
        
        elif 'tab' in query:
            pyautogui.hotkey('command', 'w')

        elif 'close it' in query:
            pyautogui.keyDown('command')
            pyautogui.keyUp('q')
            pyautogui.keyDown('q')
            pyautogui.keyUp('command')
        
        elif 'close tab' in query:
            pyautogui.keyDown('command')
            pyautogui.keyUp('w')
            pyautogui.keyDown('w')
            pyautogui.keyUp('command')
                
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my words' in query:
            speak("After you sire!")
            repeatwords()

        elif 'open library' in query:
            speak('Library is ready')
            dic()
            speak("Exiting library")

        elif 'how to spell' in query:
            spell(query)
        
        elif 'how to pronounce' in query:
            pronounce(query)

        elif 'set alarm' in query:
            time.sleep(10)
            

        elif 'open translator' in query:
            translator(query)

        elif 'remember it' in query:
            rememberit(query)

        elif 'what do you remember' in query:
            rememberfunciton()

        elif 'search' in query:
            googli(query)

        elif 'temperature of' in query:
            temp(query)


taskexe()