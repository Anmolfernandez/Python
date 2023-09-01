import requests
import json
import os
import win32com.client as wincom

city = input("enter the name of the city\n ")

url = f"https://api.weatherapi.com/v1/current.json?key=b2c006c5996144e2b9c92347230107&q={city}"
speak =wincom.Dispatch("SAPI.SpVoice")
text = "'the current weather in {city}is {w} degrees'.using win32com.client"
speak.Speak(text)
r = requests.get(url)
print(r.text)
wdic =  json.loads(r.text)
w = wdic["current"]["temp_c"]
