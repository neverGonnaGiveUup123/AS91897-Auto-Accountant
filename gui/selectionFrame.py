import customtkinter

class selectOutput(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.testTextBox = customtkinter.CTkTextbox(self)
        self.testTextBox.insert("0.0", "Hello world")
        self.testTextBox.pack()