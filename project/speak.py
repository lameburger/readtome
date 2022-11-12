# tts library
import pyttsx3
import tkinter 
# declare speaker object
speaker = pyttsx3.init()
#Set speed 
speaker.setProperty('rate', input("rate: "))
# Set volume 0-1
speaker.setProperty('volume', input("volume from 0-1: "))
# Set text
text = input("text: ")
# Set voice with path ex: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', input("path: ")
#Speak
speaker.say(text)
speaker.runAndWait()
# 