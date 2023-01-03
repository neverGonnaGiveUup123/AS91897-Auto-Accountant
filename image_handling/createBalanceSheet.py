import pytesseract
import re
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

imgText = pytesseract.image_to_string(Image.open("images/test.jpg"))

print(imgText)

splitText = imgText.split()

print(splitText)

currentAssets = {
    'Bank' : 0,
    'Accounts Receivable' : 0,
    'Prepayments' : 0,
    'Accrued Income' : 0,
    'Inventory on hand' : 0,
}

for i in splitText:
    if re.search('Bank',i) != None:
        newValue = splitText[splitText.index(i) + 1].replace(',', '')
        print(newValue)
        currentAssets['Bank'] = int(newValue)
print(currentAssets)