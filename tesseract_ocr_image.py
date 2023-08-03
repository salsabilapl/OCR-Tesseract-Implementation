# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import the necessary packages
from PIL import Image
import pytesseract
import cv2

#declarate the tesseract execuble path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image_to_ocr = cv2.imread('images/testing/fox-sample1.png')

#preprocessing the image
# step 1 : convert to grey scale
preprocessing_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
# step 2 : Do binary and otsu thresholding
#preprocessing_img = cv2.threshold(preprocessing_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, preprocessing_img = cv2.threshold(preprocessing_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# step 3 : smooth the image using median blur
preprocessing_img = cv2.medianBlur(preprocessing_img, 3)

#save the preprocessing image to convert to PIL image
cv2.imwrite("temp_img.jpg", preprocessing_img)

#load the image as a PIL/Pillow Image
preprocessing_pil_img = Image.open('temp_img.jpg')

#pass the pil image to tesseract to do OCR
text_extracted = pytesseract.image_to_string(preprocessing_pil_img)

#print the text
print(text_extracted)

#display the original image

cv2.imshow("Actual Image", image_to_ocr)
cv2.waitKey(0)
cv2.destroyAllWindows()