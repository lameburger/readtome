import pyttsx3
import os 
from PIL import Image
from pytesseract import pytesseract
import requests
from io import BytesIO
import base64
import cv2

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
    image_to_text('page.jpg')
    with open('page.txt') as f:
        text = f.read().replace('\n', '')
    text_to_speech(text, language)

def b64_to_image(encoded_data):
    reduced_encoded_data = encoded_data[21:]
    decoded_data=base64.b64decode((reduced_encoded_data))

    snapshot = open('snapshot.jpg', 'wb')
    snapshot.write(decoded_data)
    snapshot.close()

def crop(x1, y1, x2, y2):
    b64_to_image(encoded_data)
    img = cv2.imread("snapshot.jpg")
    # Cut image
    cut_img = img[y1: y2, x1: x2]
    cv2.imshow("image", img)
    cv2.imshow("cutimage", cut_img)
    cv2.waitKey(0)


def killfiles():
    os.remove("page.txt")
    os.remove("snapshot.jpg")
    os.remove("page.jpg")

