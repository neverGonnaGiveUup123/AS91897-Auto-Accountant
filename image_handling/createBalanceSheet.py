import re
import pandas as pd
import os
from readTrialBalance import readTrialBalance

# trialBalance = readTrialBalance('images/test.jpg')
# splitText = trialBalance.splitStringTrialBalance()

# print(splitText)

class createBalanceSheet:
    def __init__(self,trialBalance,splitText) -> None:
        self.trialBalance = trialBalance
        self.splitText = splitText
    
    def set_dict_values(self) -> None:
        for items in self.splitText:
            pass
    
    def find_values():
        key_words = []
        jumps = []
        for i in zip(key_words,jumps):
            pass


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

# def get_num(dictReference, dictKey, specifyJump):
#     newValue = splitText[splitText.index(i) + specifyJump].replace(',', '')
#     dictReference[str(dictKey)] = int(newValue.replace('$', ''))

# def check_trial_balance():
#     for j in currentAssets.keys():
#         if re.search(j, i) != None:
#             get_num(currentAssets, j, 1)
#     if re.search('Receivable', i) != None:
#         get_num(currentAssets, "Accounts Receivable",1)
#     if re.search('Income', i) != None:
#         get_num(currentAssets, "Accrued Income",1)
#     if re.search("hand", i) != None:
#         get_num(currentAssets, "Inventory on hand",5)
#     if re.search("Shares", i) != None:
#         get_num(investments, "Shares", 3)

# for i in splitText:
#     check_trial_balance()
    
print(currentAssets)

CAdf = pd.DataFrame.from_dict(currentAssets, orient='index')
CAdf.index.name = "Test"
print(CAdf)

try:
    os.remove(f"{os.getcwd()}/output_file/output.csv")
except FileNotFoundError:
    CAdf.to_csv('output_file/output.csv')

if os.path.exists(f"{os.getcwd()}/output_file/output.csv") == False:
    CAdf.to_csv('output_file/output.csv')