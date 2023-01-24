import pytesseract
from PIL import Image

class readTrialBalance:
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

    def __init__(self, image: str) -> None:
        self.image = image

    def splitStringTrialBalance(self) -> list:
        trialBalance = pytesseract.image_to_string(Image.open(self.image))
        return trialBalance.split()