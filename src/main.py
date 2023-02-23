from image_handling.createBalanceSheet import createBalanceSheet

def main():
    createBalanceSheet().set_dict_values(createBalanceSheet.ca_key_words)

    balance_sheet = createBalanceSheet().return_balance_sheet()
    print(balance_sheet)
    createBalanceSheet().create_csv(balance_sheet)
    # createBalanceSheet().test()

if __name__ == '__main__':
    main()

# from gui.mainGui import App
# import customtkinter

# app = App()
# app.mainloop()

