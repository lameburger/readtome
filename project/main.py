import os 

while True:
    # Scans book and outputs sample.jpg
    os.system("python scan.py")
    # Converts sample.jpg to page.txt
    os.system("python read.py")
    # Converts page.txt to audio
    os.system("python speak.py")