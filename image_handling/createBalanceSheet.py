import re
import pandas as pd
import os



class createBalanceSheet:
    from image_handling.readTrialBalance import readTrialBalance
    trialBalance = readTrialBalance('images/test.jpg')
    trialBalanceList = trialBalance.splitStringTrialBalance()
    
    def set_dict_values(self, reference: dict) -> None:
        for items in self.trialBalanceList:
            returned_value = self.find_values(self, items, self.trialBalanceList)
            if returned_value != None:
                for i in reference.keys():
                    if re.search(returned_value[1], i) != None:
                        reference[i] = returned_value[0]

    def find_values(self, items: str, text_list: list) -> int:
        key_words = ['Bank', 'Receivable', 'Prepayments', 'Income', 'hand']
        jumps = [1, 1, 1, 1, 5]
        for k, j in zip(key_words,jumps):
            if re.search(k, items) != None:
                selected_val = text_list[text_list.index(items) + j].replace(',', '')
                return selected_val.replace('$', ''), k

currentAssets = {
    'Bank' : 0,
    'Accounts Receivable' : 0,
    'Prepayments' : 0,
    'Accrued Income' : 0,
    'Inventory on hand' : 0,
}

createBalanceSheet.set_dict_values(self=createBalanceSheet,reference=currentAssets)

investments = {
    'shares' : 0,
}

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