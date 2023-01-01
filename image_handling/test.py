import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

print(pytesseract.image_to_string(Image.open("images/test.jpg")))