#A fish appears in 1 of 9 positions, the player will choose what position the fish is in

#"random" positions for FISH based on pi
posSelect = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]

i = 0 #iterator
score = 0   #set score

while(1):
    #test for restart condition (maintain their score though)
    if(i == 23): 
        i = 0
    #list of posible positions
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    
    #display score
    print("Fish Clicked: ", score) 
    print()

    #fish inserted into given position
    arr[posSelect[i]-1] = "FISH" 

    #display list in row/column format
    print(arr[0], " ", arr[1], " ",  arr[2])
    print(arr[3], " ", arr[4], " ", arr[5]) 
    print(arr[6], " ", arr[7], " ", arr[8]) 

    print()
    print("Where is the fish?")

    #take user input (this is where you would "click" the fish)
    usrSelect = input() 

<<<<<<< Updated upstream
    #test for win condition
    if(int(usrSelect) == (posSelect[i])): 
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG!")
    
    #iterate 
    i = i + 1
=======
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
>>>>>>> Stashed changes
