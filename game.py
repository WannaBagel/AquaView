import tkinter as tk
#A fish appears in 1 of 9 positions, the player will choose what position the fish is in

root = tk.Tk()

root.geometry("800x500")
root.title("AquaView")

label = tk.Label(root, text="Click A Fish!", font=('Arial', 18))
label.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

def displayGrid(ps):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers[ps-1] = "FISH"

    btn0 = tk.Button(buttonFrame, text =numbers[0], font=('Arial', 18))
    btn0.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    btn1 = tk.Button(buttonFrame, text =numbers[1], font=('Arial', 18))
    btn1.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    btn2 = tk.Button(buttonFrame, text =numbers[2], font=('Arial', 18))
    btn2.grid(row=0, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

    btn3 = tk.Button(buttonFrame, text =numbers[3], font=('Arial', 18))
    btn3.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    btn4 = tk.Button(buttonFrame, text =numbers[4], font=('Arial', 18))
    btn4.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    btn5 = tk.Button(buttonFrame, text =numbers[5], font=('Arial', 18))
    btn5.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

    btn6 = tk.Button(buttonFrame, text =numbers[6], font=('Arial', 18))
    btn6.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    btn7 = tk.Button(buttonFrame, text =numbers[7], font=('Arial', 18))
    btn7.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    btn8 = tk.Button(buttonFrame, text =numbers[8], font=('Arial', 18))
    btn8.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

    buttonFrame.pack(fill='x')


#"random" positions for FISH based on pi
posSelect = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]

i = 0 #iterator
score = 0   #set score

while(1):
    #test for restart condition (maintain their score though)
    if(i == 23): 
        i = 0
    
    #display score
    print("Fish Clicked: ", score) 
    print()

    #display list in row/column format
    displayGrid(posSelect[i])

    print()
    print("Where is the fish?")

    #take user input (this is where you would "click" the fish)
    usrSelect = input() 

    #test for win condition
    if(int(usrSelect) == (posSelect[i])): 
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG!")
    
    #iterate 
    i = i + 1