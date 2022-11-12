import pyttsx3
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = 'page.jpg'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

def image_to_text(path_to_image):
    #Open image with PIL
    image = Image.open(path_to_image)

    text = pytesseract.image_to_string(image)

    book = open("page.txt", "x")
    book.write(text)
    book.close()

def text_to_speech(text, gender, rate, volume):
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender] 

    speaker = pyttsx3.init()

    # Setting up voice rate
    speaker.setProperty('rate', rate)

    # Setting up volume level  between 0 and 1
    speaker.setProperty('volume', volume)

    # Change voices: 0 for male and 1 for female
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[code].id)

    speaker.say(text)
    speaker.runAndWait()

def main():
    #scan page and get path
    image_to_text(path_to_image)
    with open('page.txt') as f:
        text = f.read().replace('\n', '')
    text_to_speech(text, input("Gender: "), 150, .8)
    #os.remove("page.jpg")
    os.remove("page.txt")
    
if __name__ == "__main__":
    main()