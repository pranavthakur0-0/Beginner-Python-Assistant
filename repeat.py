from takecommand import takecommand
def repeatwords():
    while(True):
        words = takecommand()
        if 'exit' in words:
            break
        
        else:
            speak(words)