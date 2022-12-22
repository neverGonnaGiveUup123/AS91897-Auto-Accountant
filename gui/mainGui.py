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

        self.title("minimal example app")
        self.geometry(f"{400}x{500}")
        self.minsize(400,500)
        self.maxsize(400,500)

        self.logoImage = customtkinter.CTkImage(light_image=Image.open("images/AutoAccountantLogo1.png"), 
        dark_image=Image.open("images/AutoAccountantLogo1.png"), 
        size=(380,80))
        
        self.logoLabel = customtkinter.CTkLabel(master=self,image=self.logoImage,text="")
        self.logoLabel.pack()

        self.test = selectOutput(self)
        self.test.pack()

        self.format = selectFormat(self)
        self.format.pack()

        self.trialBalance = selectTrialBalance(self)
        self.trialBalance.pack()

        self.submitButton = customtkinter.CTkButton(self,width=100,height=24,fg_color="#345eeb",text="Submit", hover_color="#340eeb")
        self.submitButton.pack(pady=8)

if __name__ == "__main__":
    app = App()
    app.mainloop()