import customtkinter
import tkinter
from tkinter import WORD, ttk

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

        self.combobox_var = tkinter.StringVar()

        self.combobox = ttk.Combobox(
            master=self,
            values=["PDF", "XLSX", "CSV"],
            textvariable=self.combobox_var,
            state='readonly',
            
        )

        self.combobox.bind("<<ComboboxSelected>>",lambda e: self.testTextBox.focus())
        self.combobox.pack(pady=10)

    def return_combobox(self):
        return self.combobox_var

selectFormat(customtkinter.CTk()).return_combobox()