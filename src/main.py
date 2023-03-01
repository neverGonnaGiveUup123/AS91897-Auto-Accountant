from image_handling.createBalanceSheet import createBalanceSheet
from image_handling.readTrialBalance import readTrialBalance

def main():
    trial_balance = readTrialBalance()
    trial_balance.set_image('src/images/test.jpg')
    trial_balance.create_dict()

    balance_sheet_class = createBalanceSheet()
    balance_sheet_class.set_dict_values(balance_sheet_class.ca_key_words)

    print(balance_sheet_class.return_balance_sheet())
    balance_sheet_class.create_csv(balance_sheet_class.return_balance_sheet())

    # balance_sheet_class.test()

    print(balance_sheet_class.return_trial_balance_list())

if __name__ == '__main__':
    main()


