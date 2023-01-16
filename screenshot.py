from datetime import datetime
import pyautogui
def screen():
    tame=(datetime.today().strftime(" %Y-%m-%d at %I.%M.%S %p"))
    pyautogui.screenshot('/Users/pranavthakur/Desktop/Screenshot'+str(tame)+'.png')