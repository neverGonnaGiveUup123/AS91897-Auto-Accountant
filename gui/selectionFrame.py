import customtkinter
from tkinter import WORD

class selectOutput(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 360
        self.height = 210
        self._corner_radius = 0
        
        self.testTextBox = customtkinter.CTkTextbox(self,
        width=400,
        height=100,
        corner_radius=5,
        fg_color= "#345eeb",
        border_spacing=10,
        wrap=WORD,
        font=customtkinter.CTkFont(
            family="Helvetica", 
            size=22, 
            weight="bold"
            ),
        )
        self.testTextBox.insert("0.0", "What file would you like Auto Accountant to complete?")
        self.testTextBox.configure(state="disabled")
        self.testTextBox.tag_config(tagName="tag_name",justify="center")
        self.testTextBox.pack(padx=20, pady=20)

        combobox_var = customtkinter.StringVar(value="Balance Sheet")

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        combobox = customtkinter.CTkComboBox(
            master=self,
            values=["Balance sheet", "Financial statement"],
            command=combobox_callback,
            variable=combobox_var,
            width=150)
        combobox.pack(pady=20)

