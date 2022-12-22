import customtkinter
from tkinter import WORD

class selectFormat(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 360
        self.height = 140
        self._corner_radius = 0
        
        self.testTextBox = customtkinter.CTkTextbox(self,
        width=400,
        height=60,
        corner_radius=5,
        fg_color= "#345eeb",
        border_spacing=10,
        wrap=WORD,
        font=customtkinter.CTkFont(
            family="Helvetica", 
            size=14, 
            weight="bold"
            ),
        )
        self.testTextBox.insert("0.0", "What format would you like this file in?")
        self.testTextBox.configure(state="disabled")
        self.testTextBox.tag_config(tagName="tag_name",justify="center")
        self.testTextBox.pack(padx=20, pady=10)

        combobox_var = customtkinter.StringVar(value="PDF")

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        combobox = customtkinter.CTkComboBox(
            master=self,
            values=["PDF", "XLSX", "CSV"],
            command=combobox_callback,
            variable=combobox_var,
            width=150,
            state="readonly",
            text_color="black")
        combobox.pack(pady=10)