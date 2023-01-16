import pywhatkit
from datetime import datetime
from takecommand import takecommand

def Whatsapp(query):
    if 'papa' in query:
        speak("tell me the message")
        msg = takecommand()
        msge =  "{}".format(msg)
        print(msge)
        hour = int(datetime.datetime.now().strftime('%H'))
        print(hour)
        minu = int(datetime.datetime.now().strftime('%M'))
        minu = minu+1
        print(minu)
        pywhatkit.sendwhatmsg("+917018220921",msg,hour,minu,3)
    if 'mukul' in query:
        speak("tell me the message")
        msg = takecommand()
        msge =  "{}".format(msg)
        print(msge)
        hour = int(datetime.datetime.now().strftime('%H'))
        print(hour)
        minu = int(datetime.datetime.now().strftime('%M'))
        minu = minu+1
        print(minu)
        pywhatkit.sendwhatmsg("+918580450639",msg,hour,minu,3)
    
    else:
        speak("tell the number please")
        phone = takecommand()
        phone = str(phone.replace(' ', ""))
        ph = "+91" + phone
        speak("tell me the message")
        msg = takecommand()
        msge =  "{}".format(msg)
        print(msge) 
        hour = int(datetime.datetime.now().strftime('%H'))
        print(hour)
        minu = int(datetime.datetime.now().strftime('%M'))
        minu = minu+1
        print(minu)
        pywhatkit.sendwhatmsg(phone,msg,hour,minu,3)



def whatsapp(query):
    query = query.replace('WhatsApp', "" )
    query = query.replace('send', "" )
    query = query.replace('message', "")
    query = query.replace('to', "")
    print(query)
    Whatsapp(query)