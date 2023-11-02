from tkinter import *
from PIL import ImageTk, Image  # pip install pillow

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()