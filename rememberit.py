from speak import speak

def rememberit(query):
    remembermsg = query.replace('remember it ', '')
    remembermsg = query.replace('ok', '')
    remembermsg = query.replace('friday ', '')
    speak('Storing it into the memeory')
    remember = open('data.txt', 'w')
    remember.write(remembermsg)
    remember.close()