from speak import speak

def listToString(s): 
    str1 = ", " 
    return (str1.join(s))

def split(word):
    return list(word)

def spell(query):
    query = query.replace('how to spell ', "")
    query = query.replace('a word ', "")
    query = query.replace('the word ', "")
    s = split(query)
    s = listToString(s)
    speak(s) 