from PIL import Image
import customtkinter
from selectionFrame import selectOutput

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400,300)

        self.logoImage = customtkinter.CTkImage(light_image=Image.open("images/AutoAccountantLogo1.png"), 
        dark_image=Image.open("images/AutoAccountantLogo1.png"), 
        size=(380,80))
        
        self.logoLabel = customtkinter.CTkLabel(master=self,image=self.logoImage,text="")
        self.logoLabel.pack()

        self.test = selectOutput(self)
        self.test.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()