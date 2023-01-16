from speak import speak
from takecommand import takecommand
import sys 
import subprocess 
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def music():
    speak("tell the song name please")
    musicname = takecommand()

    if 'let me love you' in musicname:
        address = '/Users/pranavthakur/songs/Let-Me-Love-You_320(PaglaSongs).mp3'
        open_file(address)  
      
    else:
        pywhatkit.playonyt(musicname)