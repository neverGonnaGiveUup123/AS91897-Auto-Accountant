import pytesseract
import re
import pandas as pd
import os
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

investments = {
    'shares' : 0,
}

def get_num(dictReference, dictKey, specifyJump):
    newValue = splitText[splitText.index(i) + specifyJump].replace(',', '')
    dictReference[str(dictKey)] = int(newValue.replace('$', ''))

def check_trial_balance():
    for j in currentAssets.keys():
        if re.search(j, i) != None:
            get_num(currentAssets, j, 1)
    if re.search('Receivable', i) != None:
        get_num(currentAssets, "Accounts Receivable",1)
    if re.search('Income', i) != None:
        get_num(currentAssets, "Accrued Income",1)
    if re.search("hand", i) != None:
        get_num(currentAssets, "Inventory on hand",5)
    if re.search("Shares", i) != None:
        get_num(investments, "Shares", 3)

for i in splitText:
    check_trial_balance()
    
print(currentAssets)

CAdf = pd.DataFrame.from_dict(currentAssets, orient='index')
print(CAdf)

try:
    os.remove(f"{os.getcwd()}/output_file/output.csv")
except FileNotFoundError:
    with open('output_file/output.csv', 'a', encoding='utf-8') as file:
        file.write("Current Assets")
        file.write(f"{str(CAdf)}\n")

if os.path.exists(f"{os.getcwd()}/output_file/output.csv") == False:
    with open('output_file/output.csv', 'a', encoding='utf-8') as file:
        file.write("Current Assets")
        file.write(f"{str(CAdf)}\n")