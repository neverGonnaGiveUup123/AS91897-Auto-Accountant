import customtkinter
import tkinter
from tkinter import WORD, ttk

class selectTrialBalance(customtkinter.CTkFrame):
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
        self.testTextBox.insert("0.0", "Select trial balance file. If it's a photo, make sure it is clear.")
        self.testTextBox.configure(state="disabled")
        self.testTextBox.tag_config(tagName="tag_name",justify="center")
        self.testTextBox.pack(padx=20, pady=10)

        combobox_var = tkinter.StringVar()

        combobox = ttk.Combobox(
            master=self,
            values=["Will change this in the future", " "],
            textvariable=combobox_var,
            state='readonly',
            
        )

        combobox.bind("<<ComboboxSelected>>",lambda e: self.testTextBox.focus())
        combobox.pack(pady=10)