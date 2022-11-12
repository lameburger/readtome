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
with open('page.txt') as f:
    text = f.read().replace('\n', '')
#Speak
speaker.say(text)
speaker.runAndWait()

