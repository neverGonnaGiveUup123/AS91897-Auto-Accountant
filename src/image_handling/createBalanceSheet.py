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
    ca_key_words = [('Bank', 1), ('Receivable', 1),('Prepayments', 1), ('Income', 1), ('hand', 5)]
    nca_key_words = [('Shares', 3)]
    
    def set_dict_values(self,key_words: list) -> None:
        for items in self.trialBalanceList:
            returned_value = self.find_values(items, self.trialBalanceList, key_words)
            if returned_value is not None:
                print(returned_value)
                for i in self.balance_sheet_dict.keys():
                    if re.search(returned_value[1], i) != None:
                        self.balance_sheet_dict[i][self.determine_column(key_words, self.trialBalanceList)] = returned_value[0]

    def find_values(self, items: str, text_list: list, key_words: list) -> int:
        for k, j in key_words:
            if re.search(k, items) is not None:
                selected_val = text_list[text_list.index(items) + j].replace(',', '')
                return selected_val.replace('$', ''), k
    
    def determine_column(self, key_words: list, trial_balance_list: list):
        e = []
        for words, _ in key_words:
            for i in trial_balance_list:
                if re.search(words, i) is not None:
                    e.append(words)
        print(e)
        if len(e) > 1:
            return 0
        else:
            return 1
    
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