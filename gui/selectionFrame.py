import customtkinter

class selectOutput(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 100
        
        self.testTextBox = customtkinter.CTkTextbox(self,
        width=400,
        height=100,
        corner_radius=0, 
        font=customtkinter.CTkFont(
            family="Helvetica", 
            size=27, 
            weight="bold"
            ),
        )
        self.testTextBox.insert("0.0", "What file would you like Auto Accountant to complete?")
        self.testTextBox.configure(state="disabled")
        self.testTextBox.pack()

        combobox_var = customtkinter.StringVar(value="option 2")  # set initial value

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        combobox = customtkinter.CTkComboBox(
            master=self,
            values=["option 1", "option 2"],
            command=combobox_callback,
            variable=combobox_var)
        combobox.pack(pady=10)