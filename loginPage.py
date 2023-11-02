from tkinter import *
from PIL import ImageTk, Image  # pip install pillow

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('800x800')
        self.window.resizable(0, 0) # Makes window fixed size

        # /////////// Background /////////// #

        self.bg_pic = Image.open('AV_Images\\tank_background.jpg') # get image from directory
        photo = ImageTk.PhotoImage(self.bg_pic) # put bg pic into "photo"
        self.bg_panel = Label(self.window, image = photo) # create panel and put the photo as the image
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # /////////// Login Frame /////////// #

        self.login_frame = Frame(self.window, bg = '#040405', width = '400', height = '500')
        self.login_frame.place(x = '200', y = '150')

        # /////////// Text /////////////#
        self.heading = Label(self.login_frame, text = 'Aqua View', font = ('Times', 28, 'bold'), bg = '#040405', fg = 'white')
        self.heading.place(x= 100, y = 10, width= 200, height= 50)

        self.heading = Label(self.login_frame, text = 'Login', font= ('Times', 24, 'bold'), bg ='#040405', fg = 'white')
        self.heading.place(x = 150, y = 65, width = 100, height = 50)

        self.heading = Label(self.login_frame, text = 'Username', font= ('Times', 18, 'bold'), bg ='#040405', fg = 'white')
        self.heading.place(x = 10, y = 150, width = 100, height = 50)

        self.heading = Label(self.login_frame, text = 'Password', font= ('Times', 18, 'bold'), bg ='#040405', fg = 'white')
        self.heading.place(x = 10, y = 230, width = 100, height = 50)


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()