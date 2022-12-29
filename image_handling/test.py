import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sidsa\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pytesseract.exe'

print(pytesseract.image_to_string(Image.open("images/test.jpg")))