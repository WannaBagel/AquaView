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

#Function to create account
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        def create_account():
            #Close log in window
            self.login_frame.destroy()

            #Create new frame to make account
            self.create_frame = Frame(self.window, width = '400', bg = '#608da2', height = '500')
            self.create_frame.place(x = '150', y = '150')

            #Text
            self.heading = Label(self.create_frame, text = 'Username:', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
            self.heading.place(x = 10, y = 50, width = 120, height = 50)

            self.heading = Label(self.create_frame, text = 'Password:', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
            self.heading.place(x = 10, y = 140, width = 120, height = 50)

            self.heading = Label(self.create_frame, text = 'Re-Type Password:', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
            self.heading.place(x = 10, y = 230, width = 200, height = 50)

            #Entries
            user_box = Entry(self.create_frame, font = ('Arial', 12), bg ='white', fg = 'black')
            user_box.place(x = 10, y = 90, width = 375, height = 30)

            pass_box = Entry(self.create_frame, font = ('Arial', 12), bg ='white', fg = 'black')
            pass_box.place(x = 10, y = 180, width = 375, height = 30)

            pass_box2 = Entry(self.create_frame, font = ('Arial', 12), bg ='white', fg = 'black')
            pass_box2.place(x = 10, y = 270, width = 375, height = 30)

            #Button
            # Lambda command makes us wait until the button is clicked to make the new login page
            create_butt = Button(self.create_frame, text = "Create Account", bg = '#608da2', command= lambda: createUser())
            create_butt.place(x = 125, y = 350, width = 150, height = 30)

            def createUser():
                #Get string from entry boxes
                username = user_box.get()
                password = pass_box.get()
                confirmpass = pass_box2.get()
                taken = False

                # Go through usernames and make sure the entered one DNE already
                with open("Temp_users_pass", "r") as info:
                    for line in info:
                        next = line
                        useronly = next.split(":")
                        if username == useronly[0]:
                            taken = True

                # Show errors if username is taken or if passwords dont match
                if taken:       
                    self.heading = Label(self.create_frame, text = "That username is already taken", bg = '#608da2', fg = 'red')
                    self.heading.place(x = 150, y = 65, width = 200, height = 25)
                if password != confirmpass:
                    self.heading = Label(self.create_frame, text = "Passwords don't match", bg = '#608da2', fg = 'red')
                    self.heading.place(x = 150, y = 155, width = 200, height = 25)
                
                # If valid new user, write to the user database file
                if taken == False and password == confirmpass:
                    data = open("Temp_users_pass", "a")                    
                    data.write(username)
                    data.write(":")
                    data.write(password)
                    data.write("\n")
                    data.close()
                    LoginPage(window)

                

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # /////////// Login Frame /////////// #

        self.login_frame = Frame(self.window, width = '400', bg = '#608da2', height = '500')
        self.login_frame.place(x = '150', y = '150')

        # /////////// Text /////////////#
        self.heading = Label(self.login_frame, text = 'Aquaview', font = ('Arial', 28, 'bold'), bg = '#608da2', fg = 'black')
        self.heading.place(x= 100, y = 15, width= 200, height= 50)

        self.heading = Label(self.login_frame, text = 'Username', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
        self.heading.place(x = 10, y = 100, width = 120, height = 50)

        self.heading = Label(self.login_frame, text = 'Password', font= ('Arial', 16, 'bold'), bg ='#608da2', fg = 'black')
        self.heading.place(x = 10, y = 190, width = 120, height = 50)

        self.heading = Label(self.login_frame, text = "Don't have an account?", font = ('Arial', 8), bg ='#608da2', fg = 'black')
        self.heading.place(x = 12, y = 305, width = 120, height = 50)

        #/////////// Entries /////////// #

        user_box = Entry(self.login_frame, font = ('Arial', 12), bg ='white', fg = 'black')
        user_box.place(x = 10, y = 140, width = 375, height = 30)

        pass_box = Entry(self.login_frame, font = ('Arial', 12), show = '*', bg ='white', fg = 'black')
        pass_box.place(x = 10, y = 230, width = 375, height = 30)

        #//////////// Buttons ////////////// #
        login_butt = Button(self.login_frame, text = 'LOGIN', font= ('Arial', 16, 'bold'), bg = '#A2B5CD', fg = 'black')
        login_butt.place(x = 275, y = 275, width = 100, height = 25)

        remember_butt = Checkbutton(self.login_frame, text = 'Remember Me', bg = '#608da2')
        remember_butt.place(x = 12, y = 275, width = 100, height = 12)

        create_acc = Button(self.login_frame, text = 'create account', bg = '#A2B5CD', command=create_account)
        create_acc.place(x = 12, y = 340, width = 100, height = 18)



def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()