from speak import speak
from takecommand import takecommand
import nltk
from nltk.corpus import wordnet
from PyDictionary import PyDictionary as diction

def listToString(s): 
    string = ","
    return (string.join(s)) 

def repeatdic(result,prob):
    speak(f"The meaning of {prob} is {result}")
    speak('Want to ask another meaning or, shall I repeat the meaning')
    rep = takecommand()

    if 'repeat' in rep:
        repeatdic(result, prob)

    elif 'what\'s the meaning' in rep:
        dic3(rep)

    elif 'meaning of' in rep:
        dic3(rep)

    elif 'what does mean' in rep:
        dic3(rep)

    elif 'what is the meaning'in rep:
        dic3(rep)
            
    elif 'no' in rep:
        print("")

    elif 'exit' in rep:
        print("")

    elif 'quit'  in rep:
        print("")

    elif 'none' in rep:
        print("")


def dic2(result,prob):
    speak(f"The meaning of {prob} is {result}")
    time.sleep(5)
    speak('Anything you want to ask or, shall I repeat the meaning')
    rep = takecommand()
    if 'repeat' in rep:
        repeatdic(result, prob)

    elif 'what\'s the meaning' in rep:
        dic3(rep)

    elif 'meaning of' in rep:
        dic3(rep)

    elif 'what does mean' in rep:
        dic3(rep)

    elif 'what is the meaning'in rep:
        dic3(rep)

    elif 'no' in rep:
        print("")

    elif 'exit' in rep:
        print("")
        
    elif 'quit'  in rep:
        print("")

    elif 'none' in rep:
        print("")


def dic3(rep):
    while(True):
        prob = rep
        if 'meaning of'in prob:
            prob = prob.replace('meaning of', "")
            result = diction.meaning(prob)
            dic2(result,prob)

        


def repeatsyn(s):   
    speak(s)
    speak('Anything you want to ask or, shall I repeat the synonym')
    rep = takecommand()
    if 'repeat' in rep:
        repeatsyn(s)

    elif 'synonym of' in rep:
        rep = rep.replace('synonym of ', "")
        syno(rep)  

    elif 'no' in rep:
        print("")

    elif 'exit' in rep:
        print("")

    elif 'quit'  in rep:
        print("")

    elif 'none' in rep:
        print("")


def syno(prob):
    synonyms = []
    for syn in wordnet.synsets(prob):
        for lm in syn.lemmas():
             synonyms.append(lm.name()) if lm.name() not in synonyms else Non
             
    s = (set(synonyms))
    s=(listToString(s))
    speak(s)
    speak('Anything you want to ask or, shall I repeat the synonym')
    rep = takecommand()
    if 'repeat' in rep:
        repeatsyn(s)

    elif 'no' in rep:
        print("")

    elif 'exit' in rep:
        print("")

    elif 'quit'  in rep:
        print("")

    elif 'none' in rep:
        print("")


def dic():
    speak("Tell me what you want to ask")
    while(True):
        prob = takecommand() 
        if 'meaning of'in prob:
            prob = prob.replace('meaning of', "")
            result = diction.meaning(prob)
            dic2(result,prob)
        elif 'synonym of' in prob:
            prob = prob.replace('synonym of ', "")
            print(prob)
            syno(prob)

    