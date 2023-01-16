import requests
from bs4 import BeautifulSoup
from speak import speak
def temperature(query):
    search = f'temperature of {query}'
    url = f'https://www.google.com/search?q={search}'
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find('div',class_= "BNeawe").text
    speak(f'The temperature ouside is {temperature}')

def temp(query):
    query = query.replace('friday what\'s the temperature of ',"")
    query = query.replace('friday', '')
    query = query.replace('temperature of ', '')
    temperature(query)