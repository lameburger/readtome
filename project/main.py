import pyttsx3
import os 
from PIL import Image
from pytesseract import pytesseract
import requests
from io import BytesIO
import base64
import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types
import sys
import glob


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

def identify(encoded_data):
    b64_to_image(encoded_data)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'fresh-capsule-368416-338e08784eb3.json'

    client = vision.ImageAnnotatorClient()

    path = r'snapshot.jpg'

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    img = cv2.imread("snapshot.jpg")
    height, width, _ = img.shape
    
    for object_ in objects:
        vertices = []
        for vertex in object_.bounding_poly.normalized_vertices:
            # Puts vertices into list
            vertices.append((vertex.x, vertex.y))
        # Find bottom left and top left vertices
        min = sys.maxsize 
        max = 0 
        for tuple in vertices:
            if tuple[0] + tuple[1] < min:
                mintuple = (tuple[0], tuple[1]) 
                min = tuple[0] + tuple[1]
            if tuple[0] + tuple[1] >= max:
                maxtuple = (tuple[0], tuple[1]) 
                max = tuple[0] + tuple[1]
        # add rectangle and text
        img = cv2.rectangle(img, (round(mintuple[0]*width), round(mintuple[1]*height)), (round(maxtuple[0]*width), round(maxtuple[1]*height)), (36, 255, 12), 1)
        cv2.putText(img, object_.name, (round(mintuple[0]*width)+1, round(mintuple[1]*height)+16), cv2.FONT_HERSHEY_SIMPLEX, .7, (36,255,12), 2)
        crop(round(mintuple[0]*width), round(mintuple[1]*height), (round(maxtuple[0]*width), round(maxtuple[1]*height), object_.name))
    cv2.imwrite("identified.jpg", img)

def killfiles():
    removingjpg= glob.glob('project/*.jpg')
    for i in removingjpg:
        os.remove(i)
    removingtxt = glob.glob('project/*.txt')
    for i in removingtxt:
        os.remove(i)

def crop(x1, y1, x2, y2, name):
    img = cv2.imread(f"cropped{name}{x1}{y1}{x2}{y2}.png")
    rows, cols, _ = img.shape
    cropped_image = img[x1: x2, y1: y2]
