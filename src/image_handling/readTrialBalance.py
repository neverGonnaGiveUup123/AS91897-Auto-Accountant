import pytesseract
from PIL import Image
import re
import json

class readTrialBalance:
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

    def set_image(self, image_path):
        self.image = image_path

    def return_image(self):
        return self.image

    def splitStringTrialBalance(self) -> list:
        trialBalance = pytesseract.image_to_string(Image.open(self.image))
        return trialBalance.split()
    
    def create_dict(self):
        sorting_array = []
        with open('src/data/key_word_list.json', 'r') as file:
            key_word_list = json.load(file)
        for word in self.splitStringTrialBalance():
            for term, category in key_word_list:
                if re.search(term, word) is not None:
                    sorting_array.append((term, category))
        sorting_array.sort(key=self.sorting_array_func)
        print(sorting_array)
        self.add_dict_item(sorting_array)

    def add_dict_item(self, sorted_list):
        balance_sheet_dict = {}
        with open("src/data/test_json.json", "w") as file:
            for counter, obj in enumerate(sorted_list):
                term, category = obj
                if category == 0:
                    if counter == 0:
                        balance_sheet_dict["Current Assets"] = [" "]
                    else:
                        balance_sheet_dict[term] = [" ", " ", " "]
                elif category == 1:
                    balance_sheet_dict["Non-current assets"] = [" "]
                    balance_sheet_dict[term] = [" ", " ", " "]
            json.dump(balance_sheet_dict, file)


        # with open("src/data/balance_sheet_data", 'w') as file:
        #     dict_file = json.load(file)
        #     json.dump()

    def sorting_array_func(self, e):
        # 0 = current asset
        return e[1]
        
                    