from dataclasses import dataclass
import dacite
import requests
import speech_recognition as sr
from playsound import playsound
import wget
import os
import time
import sys

voiceAPIkey = ""
sourceLangChoice = ['nil', 'nil']
targetLangChoice = ['nil', 'nil']

sourceLang = input("What language do you speak? (Enter 1, 2 or 3 and press enter)\n1: English\n2: Dutch\n3: German\n")
if sourceLang == "1":
    sourceLangChoice = ["en-US", "en"]
elif sourceLang == "2":
    sourceLangChoice = ["nl-NL", "nl"]
elif sourceLang == "3":
    sourceLangChoice = ["de-DE", "de"]

targetLang = input("What language will translation be? (Type 1, 2 or 3 and press enter)\n1: English\n2: Dutch\n3: German\n")
if targetLang == "1":
    targetLangChoice = ["en-US", "en"]
elif targetLang == "2":
    targetLangChoice = ["nl-NL", "nl"]
elif targetLang == "3":
    targetLangChoice = ["de-DE", "de"]

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    try:
        print("Text: " + r.recognize_google(audio_text, language=sourceLangChoice[0]))
    except:
        print("Sorry, I did not get that")

audio = r.recognize_google(audio_text, language=sourceLangChoice[0])

url = "https://libretranslate.de/translate"
headers = {"Content-Type": "application/json"}

data = {
    "q": audio,
    "source": sourceLangChoice[1],
    "target": targetLangChoice[1],
    "format": "text",
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())


@dataclass
class Text:
    translatedText: str


@dataclass
class Dat:
    translatedText: str


data = response.json()

dat: Dat = dacite.from_dict(Dat, data)

textWithoutDot = dat.translatedText.replace('.', '')
if textWithoutDot.__contains__("♪"):
    print("Unable to process voice... Try again.")
    time.sleep(5)
    sys.exit(0)

url = "http://api.voicerss.org/?key="+ voiceAPIkey + "&hl=" + targetLangChoice[0].lower() + "&src=" + textWithoutDot
AudioURL = url.replace(' ', '%20')
AudioURL = AudioURL.replace('♪', '')
print("Using URL:")
print(AudioURL)

filename = wget.download(AudioURL, 'ttsSound.wav')
playsound(filename)
os.remove('ttsSound.wav')
