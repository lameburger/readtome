from main import b64_to_image
import cv2
import numpy as np
import os
# Creates snapshot
b64_to_image()
# Detect book corners

'''
# bottom left
x1 = 0
y1 = 0
# top right
x2 = 320
y2 = 240
'''

# Crop
img = cv2.imread("snapshot.jpg")
rows, cols, _ = img.shape
print(rows)
print(cols)

# Cut image
cut_img = img[y1: y2, x1: x2]
cv2.imshow("image", img)
cv2.imshow("cutimage", cut_img)

cv2.waitKey(0)

#