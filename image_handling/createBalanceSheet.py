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

def get_num(dictReference):
    newValue = splitText[splitText.index(i) + 1].replace(',', '')
    currentAssets[str(dictReference)] = int(newValue)

def check_trial_balance():
    for j in currentAssets.keys():
        if re.search(j, i) != None:
            get_num(j)

for i in splitText:
    check_trial_balance()
    if re.search("^CA.*Accounts$", i) != None:
        testList = ''.join(splitText[splitText.index(i):splitText.index(i) + 2])
print(testList)
print(currentAssets)