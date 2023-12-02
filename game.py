import tkinter as tk
import random

#score keeping
score = 0   
#iterator
i = 0     
#pi to 23 places for "random" number generation
answer = [random.randint(1,9) for int in range(30)]
#answer(i) = [Row,Column] coordinates of fish
fishLocationEncoder = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
#fishButton global variable 
fishButton = 0

#initialize window
root = tk.Tk()
root.geometry("600x500")
root.resizable(0,0)
root.config(background='#608da2')
root.title("Aquaview")

#Display Game Instructions and Score
label2 = tk.Label(root, text="Click A Fish!", font=('Arial', 18), background='#608da2')
label2.pack(padx=20, pady=20)
label = tk.Label(root, text="Score: " + str(score), font=('Arial', 18), background='#608da2')
label.pack(padx=20, pady=20)

#innitialize grid for buttons
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

#Call to update score and move the fish
def fishClicked():
    global score
    global clickThis
    global i
    score = score + 1
    label.config(text="Score: " + str(score))
    moveFish()
    i = i + 1
    testI()

#Test if iterator needs to be reset
def testI():
    global i
    if(i == len(answer)-1):
        i = 0

#move the position of the fish
def moveFish():
    global fishLocationEncoder
    global i
    global fishButton

    fishButton.grid(row=fishLocationEncoder[answer[i]-1][0], column=fishLocationEncoder[answer[i]-1][1], sticky=tk.NS)

#call to initialize the button containing the fish
def initializeFish():
    global fishButton
    global fishLocationEncoder
    global i

    fishButton = tk.Button(buttonFrame, text= "🐠", font=('Arial', 30), command=fishClicked, background='#608da2', fg='Dark Orange')
    fishButton.grid(row=fishLocationEncoder[answer[i]-1][0], column=fishLocationEncoder[answer[i]-1][1], sticky=tk.NS)

#call from main to create empty buttons and begin tk main loop
def displayButtons():

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=0, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=0, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=0, column=2, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=1, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=1, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=1, column=2, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=2, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=2, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 30), background='#608da2')
    button1.grid(row=2, column=2, sticky=tk.NS)

    initializeFish()
    buttonFrame.config(background='#608da2')
    buttonFrame.pack(fill='both')

    root.mainloop()


#main:
displayButtons()