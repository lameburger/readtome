# tts library
import pyttsx3
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



#Get voices, should check on pi
'''
voices = converter.getProperty('voices')
  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)
'''