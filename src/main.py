from image_handling.createBalanceSheet import createBalanceSheet

def main():
    print(createBalanceSheet().return_trial_balance_list())
    createBalanceSheet().set_dict_values()

    balance_sheet = createBalanceSheet().return_balance_sheet()
    print(balance_sheet)
    createBalanceSheet().create_csv(balance_sheet)

if __name__ == '__main__':
    main()

# from gui.mainGui import App
# import customtkinter

# app = App()
# app.mainloop()

