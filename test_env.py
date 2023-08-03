# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import the necessary packages
import pytesseract
import pkg_resources

#declarate the tesseract execuble path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print(pkg_resources.working_set.by_key['pytesseract'].version)