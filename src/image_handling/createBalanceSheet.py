import re
import pandas as pd
import os
import json

class createBalanceSheet:
    with open(f'{os.getcwd()}/src/data/balance_sheet_data.json', 'r') as file:
        balance_sheet_dict = json.load(file)
    from image_handling.readTrialBalance import readTrialBalance
    trialBalance = readTrialBalance('src/images/test.jpg')
    trialBalanceList = trialBalance.splitStringTrialBalance()
    
    def set_dict_values(self) -> None:
        for items in self.trialBalanceList:
            returned_value = self.find_values(items, self.trialBalanceList)
            if returned_value != None:
                print(returned_value)
                for i in self.balance_sheet_dict.keys():
                    if re.search(returned_value[1], i) != None:
                        self.balance_sheet_dict[i][1] = returned_value[0]

    def find_values(self, items: str, text_list: list) -> int:
        key_words = ['Bank', 'Receivable', 'Prepayments', 'Income', 'hand', 'Shares']
        jumps = [1, 1, 1, 1, 5, 3]
        for k, j in zip(key_words,jumps):
            if re.search(k, items) != None:
                selected_val = text_list[text_list.index(items) + j].replace(',', '')
                return selected_val.replace('$', ''), k
    
    def return_trial_balance_list(self) -> list:
        return self.trialBalanceList
    
    def return_balance_sheet(self) -> dict:
        return self.balance_sheet_dict

    def create_csv(self, balance_sheet: dict):
        df = pd.DataFrame.from_dict(balance_sheet, orient='index')
        try:
            os.remove(f"{os.getcwd()}/src/output_file/output.csv")
        except FileNotFoundError:
            df.to_csv('src/output_file/output.csv', header=False)

        if os.path.exists(f"{os.getcwd()}/src/output_file/output.csv") == False:
            df.to_csv('src/output_file/output.csv', header=False)