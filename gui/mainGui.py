import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)

        # self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        # self.button.pack(padx=20, pady=20)

        self.mainTextBox = customtkinter.CTkTextbox(master=self,width=self.winfo_width(),height=self.winfo_height()//4)
        self.mainTextBox.insert("0.0", "Hello World")
        self.mainTextBox.pack(pady = 20)

    def button_callback(self):
        print("button pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()