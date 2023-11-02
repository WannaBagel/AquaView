from tkinter import *
from PIL import ImageTk, Image  # pip install pillow

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('870x400')
        self.window.resizable(0, 0) # Makes window fixed size

        self.bg_pic = Image.open('AV_Images\\tank_background.jpg') # get image from directory
        photo = ImageTk.PhotoImage(self.bg_pic) # put bg pic into "photo"
        self.bg_panel = Label(self.window, image = photo) # create panel and put the photo as the image
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()