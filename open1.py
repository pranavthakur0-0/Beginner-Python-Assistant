import os
def app(query):
    query = query.replace('open', "" )
    query = query.replace('application', "")
    
    if 'pycharm' in query:
        os.system('open /Applications/PyCharm\ CE.app')
    
    elif 'vs code' in query:
        os.system('/Applications/Google Chrome.app')
    
    elif 'chrome' in query:
        os.system('open /Applications/Google\ Chrome.app')
    
    elif 'safari' in query:
        os.system('open /Applications/Safari.app') 
    elif 'telegram' in query:
        os.system('open /Applications/Telegram.app')