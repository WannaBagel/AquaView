import tkinter as tk

#FIXME THE FISH SHOULD BE THE ONLY ACTIONABLE CLICK, THE FISH SHOULDN'T MOVE IF YOU DON'T CLICK IT

score = 0
answer = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]
i = 0

root = tk.Tk()
root.geometry("800x500")

label2 = tk.Label(root, text="Click A Fish!", font=('Arial', 18))
label2.pack(padx=20, pady=20)

label = tk.Label(root, text="Score: " + str(score), font=('Arial', 18))
label.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)


clickThis = tk.Label(root, text= "Click: " + str(answer[i]), font=('Arial', 18))
clickThis.pack(padx=10, pady=10)

def updateScore1():
    global i
    global answer 
    if(answer[i] == 1):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore2():
    global i
    global answer 
    if(answer[i] == 2):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore3():
    global i
    global answer 
    if(answer[i] == 3):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()

def updateScore4():
    global i
    global answer 
    if(answer[i] == 4):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore5():
    global i
    global answer 
    if(answer[i] == 5):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore6():
    global i
    global answer 
    if(answer[i] == 6):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()

def updateScore7():
    global i
    global answer 
    if(answer[i] == 7):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore8():
    global i
    global answer 
    if(answer[i] == 8):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()
def updateScore9():
    global i
    global answer 
    if(answer[i] == 9):
        global score
        score = score + 1
        label.config(text="Score: " + str(score))
    i = i + 1
    testI()

def testI():
    global i
    if(i == len(answer)-1):
        i = 0
    clickThisUpdate()
    
def clickThisUpdate():
    global clickThis
    global fishLocation

    clickThis.config(text="Click: " + str(answer[i]))


def display():


    button1 = tk.Button(buttonFrame, text="1", font=('Arial', 16), command=updateScore1)
    button1.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    button2 = tk.Button(buttonFrame, text="2", font=('Arial', 16), command=updateScore2)
    button2.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    button3 = tk.Button(buttonFrame, text="3", font=('Arial', 16), command=updateScore3)
    button3.grid(row=0, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

    button4 = tk.Button(buttonFrame, text="4", font=('Arial', 16), command=updateScore4)
    button4.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    button5 = tk.Button(buttonFrame, text="5", font=('Arial', 16), command=updateScore5)
    button5.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    button6 = tk.Button(buttonFrame, text="6", font=('Arial', 16), command=updateScore6)
    button6.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

    button7 = tk.Button(buttonFrame, text="7", font=('Arial', 16), command=updateScore7)
    button7.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    button8 = tk.Button(buttonFrame, text="8", font=('Arial', 16), command=updateScore8)
    button8.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    button9 = tk.Button(buttonFrame, text="9", font=('Arial', 16), command=updateScore9)
    button9.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S)


    buttonFrame.pack(fill='both')

    root.mainloop()




display()


