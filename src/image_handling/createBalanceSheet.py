import re
import pandas as pd
import os
import json


class createBalanceSheet:
    with open(f"{os.getcwd()}/src/data/test_json.json", "r") as file:
        balance_sheet_dict = json.load(file)
    from image_handling.readTrialBalance import readTrialBalance
    trial_balance = readTrialBalance()
    trial_balance.set_image('src/images/test.jpg')
    trialBalanceList = trial_balance.splitStringTrialBalance()
    ca_key_words = [
        ["Bank", 1, 0, 0],
        ["Receivable", 1, 0, 1],
        ["Prepayments", 1, 0, 2],
        ["Income", 1, 0, 3],
        ["hand", 5, 0, 4],
        [None, 0, 0, 5],
        ["Shares", 3, 0, 6],
        [None, 0, 0, 7],
    ]

    def set_dict_values(self, key_words: list) -> None:
        for items in self.trialBalanceList:
            returned_value = self.find_values(items, self.trialBalanceList, key_words)
            if returned_value is not None:
                for i in self.balance_sheet_dict.keys():
                    if re.search(returned_value[1], i) is not None:
                        self.determine_column(self.ca_key_words, self.trialBalanceList)
                        for a, b, c, d in self.ca_key_words:
                            print(i)
                            if re.search(str(a), i) is not None:
                                self.balance_sheet_dict[i][c] = returned_value[0]
                                

    def find_values(self, items: str, text_list: list, key_words: list) -> int:
        for k, j, column, id in key_words:
            if k is not None:
                if re.search(k, items) is not None:
                    selected_val = text_list[text_list.index(items) + j].replace(
                        ",", ""
                    )
                    print(selected_val.replace("$", ""), k)
                    return selected_val.replace("$", ""), k
                
    
    def return_value(self, word, item, jumps, text_list):
        if re.search(word, item) is not None:
            selected_val = text_list[text_list.index(item) + jumps].replace(
                ",", ""
            )
            print(selected_val.replace("$", ""), word)
            return selected_val.replace("$", ""), word


    def determine_column(self, key_words: list, trial_balance_list: list):
        e = []
        global column_id

        for words, value, column_id, index in key_words:
            if words is not None:
                for i in trial_balance_list:
                    if re.search(words, i) is not None:
                        e.append(words)
            if words == None:
                print(e)
                if len(e) > 1:

                    key_words[index][2] = 0
                    e = []
                else:
                    key_words[index - 1][2] = 1
        print(self.ca_key_words)

    def test(self):
        for a,b,c,d in self.ca_key_words:
            print(type(a))

    def return_trial_balance_list(self) -> list:
        return self.trialBalanceList

    def return_balance_sheet(self) -> dict:
        return self.balance_sheet_dict

    def create_csv(self, balance_sheet: dict):
        df = pd.DataFrame.from_dict(balance_sheet, orient="index")
        try:
            os.remove(f"{os.getcwd()}/src/output_file/output.csv")
        except FileNotFoundError:
            df.to_csv("src/output_file/output.csv", header=False)

        if os.path.exists(f"{os.getcwd()}/src/output_file/output.csv") == False:
            df.to_csv("src/output_file/output.csv", header=False)
