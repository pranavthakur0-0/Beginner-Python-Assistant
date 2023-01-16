import os
def closeapp(query):
    query = query.replace('close', "" )
    query = query.replace('app', "")
    if 'pycharm' in query:
        os.close("PyCharm")
            
    elif 'vs code' in query:
        os.system('pkill Code - Insiders')
            
    elif 'chrome' in query:
        os.system("pkill Chrome")
            
    elif 'safari' in query:
        os.system("pkill Safari")
                
    elif 'telegram' in query:
        os.system("pkill Telegram")