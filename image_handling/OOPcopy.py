import pytesseract
import re
import pandas as pd
import os
from PIL import Image

class createBalanceSheet():
    def __init__(self, tesseractCMD: str) -> None:
        pytesseract.pytesseract.tesseract_cmd = tesseractCMD
        self.trialBalance = pytesseract.image_to_string(Image.open("images/test.jpg"))


print(createBalanceSheet('C:\Program Files\Tesseract-OCR/tesseract.exe').trialBalance)