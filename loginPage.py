from tkinter import *
from PIL import ImageTk, Image  # pip install pillow

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('700x800')
        self.window.resizable(0, 0) # Makes window fixed size

        # /////////// Background /////////// #

        self.bg_pic = Image.open('AV_Images\\avbg.jpg') # get image from directory
        photo = ImageTk.PhotoImage(self.bg_pic) # put bg pic into "photo"
        self.bg_panel = Label(self.window, image = photo) # create panel and put the photo as the image
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # /////////// Login Frame /////////// #

        self.login_frame = Frame(self.window, width = '400', bg = '#608da2', height = '500')
        self.login_frame.place(x = '150', y = '150')

        # /////////// Text /////////////#
        self.heading = Label(self.login_frame, text = 'Aqua View', font = ('Arial', 28, 'bold'), bg = '#608da2', fg = 'black')
        self.heading.place(x= 100, y = 15, width= 200, height= 50)

        self.heading = Label(self.login_frame, text = 'Login', font= ('Arial', 22, 'bold'), bg = '#608da2', fg = 'black')
        self.heading.place(x = 150, y = 105, width = 100, height = 50)

        self.heading = Label(self.login_frame, text = 'Username', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
        self.heading.place(x = 10, y = 150, width = 120, height = 50)

        self.heading = Label(self.login_frame, text = 'Password', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
        self.heading.place(x = 10, y = 230, width = 120, height = 50)


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()