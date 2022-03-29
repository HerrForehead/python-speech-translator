# Python Speech Translator

## Description

An application built in Python that allows the user to speak a phrase with their own voice. Which will be recognized as a string by google speech recognition, translated to a language of choice by libretranslate and then converted to a .wav by the VoiceRSS Text-To-Speech API.

## Usage

To use this application, you will have to first get your own API key at https://voicerss.org/personel. This key should be on your profile page. Paste this in the follow code, between the "s.
```
voiceAPIkey = ""
```

for best results, you will have to build the application with pyinstaller.
https://pypi.org/project/pyinstaller/
```pip install pyinstaller```
Then
```pyinstaller main.py```
Then run the main.exe file in the ./dist/main/ folder.

## Issues

Issues can be reported under the issues tab. Please be as clear as possible and give any errors you may receive.