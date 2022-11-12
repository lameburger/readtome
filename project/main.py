import pyttsx3
import os 
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

def image_to_text(path_to_image):
    #Open image with PIL
    image = Image.open(path_to_image)

    text = pytesseract.image_to_string(image)

    book = open("page.txt", "x")
    book.write(text)
    book.close()

def text_to_speech(text, language, rate=150, volume=.8):
    lang_dict = {'German': 1, 'English': 2, 'French': 4, 'Spanish': 3}
    index = lang_dict[language]

    speaker = pyttsx3.init()

    # Setting up voice rate
    speaker.setProperty('rate', rate)

    # Setting up volume level  between 0 and 1
    speaker.setProperty('volume', volume)

    # Change voices: 0 for male and 1 for female
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[index].id)

    speaker.say(text)
    speaker.runAndWait()

def image_to_speech(language):
    image_to_text('page.png')
    with open('page.txt') as f:
        text = f.read().replace('\n', '')
    text_to_speech(text, language)
    #os.remove("page.jpg")
    os.remove("page.txt")
