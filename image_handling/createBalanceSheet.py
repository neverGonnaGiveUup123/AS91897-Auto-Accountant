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

def get_num(dictReference, specifyJump):
    newValue = splitText[splitText.index(i) + specifyJump].replace(',', '')
    currentAssets[str(dictReference)] = int(newValue.replace('$', ''))

def check_trial_balance():
    for j in currentAssets.keys():
        if re.search(j, i) != None:
            get_num(j,1)

for i in splitText:
    check_trial_balance()
    if re.search('Receivable', i) != None:
        get_num("Accounts Receivable",1)
    if re.search('Income', i) != None:
        get_num("Accrued Income",1)
    if re.search("hand", i) != None:
        get_num("Inventory on hand",5)
    
print(currentAssets)