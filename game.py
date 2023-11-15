import tkinter as tk

#score keeping
score = 0   
#iterator
i = 0     
#pi to 23 places for "random" number generation
answer = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]
#answer(i) = [Row,Column] coordinates of fish
fishLocationEncoder = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
#fishButton global variable 
fishButton = 0

#initialize window
root = tk.Tk()
root.geometry("800x500")
root.config(background='Aqua')
root.title("Aquaview")

#Display Game Instructions and Score
label2 = tk.Label(root, text="Click A Fish!", font=('Arial', 18), background='Aqua')
label2.pack(padx=20, pady=20)
label = tk.Label(root, text="Score: " + str(score), font=('Arial', 18), background='Aqua')
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

    fishButton = tk.Button(buttonFrame, text= "🐠", font=('Arial', 16), command=fishClicked, background='Aqua', fg='Dark Orange')
    fishButton.grid(row=fishLocationEncoder[answer[i]-1][0], column=fishLocationEncoder[answer[i]-1][1], sticky=tk.NS)

#call from main to create empty buttons and begin tk main loop
def displayButtons():

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=0, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=0, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=0, column=2, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=1, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=1, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=1, column=2, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=2, column=0, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=2, column=1, sticky=tk.NS)

    button1 = tk.Button(buttonFrame, text="    ", font=('Arial', 16), background='Aqua')
    button1.grid(row=2, column=2, sticky=tk.NS)

    initializeFish()
    buttonFrame.config(background='Aqua')
    buttonFrame.pack(fill='both')

    root.mainloop()


#main:
displayButtons()