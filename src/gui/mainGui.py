from PIL import Image
import customtkinter

from selectionFrame import selectOutput
from formatFrame import selectFormat
from trialBalanceFrame import selectTrialBalance

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AS91897")
        self.geometry(f"{400}x{500}")
        self.minsize(400,500)
        self.maxsize(400,500)

        self.logoImage = customtkinter.CTkImage(light_image=Image.open("src/images/AutoAccountantLogo1.png"), 
        dark_image=Image.open("src/images/AutoAccountantLogo1.png"), 
        size=(380,80))
        
        self.logoLabel = customtkinter.CTkLabel(master=self,image=self.logoImage,text="")
        self.logoLabel.pack()

        self.output = selectOutput(self)
        self.output.pack()

        self.format = selectFormat(self)
        self.format.pack()

        self.trialBalance = selectTrialBalance(self)
        self.trialBalance.pack()

        def get_selected_file():
            with open('src/file_communication/SelectedFile.txt', "r") as file:
                text = file.read()
                splitText = text.split("'")
                print(splitText[1])

        self.submitButton = customtkinter.CTkButton(self,
        width=200,
        text="Submit",
        font=customtkinter.CTkFont(size=18),
        command=get_selected_file)

        self.submitButton.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()