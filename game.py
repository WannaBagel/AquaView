#basic choosing game

#"random" numbers based on pi
rowSelect = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3]
columnSelect = [2, 6, 4, 3, 3, 2, 3, 8, 4, 6, 8, 9, 7, 9, 3, 2, 6, 5, 3, 5, 1, 4, 1, 5, 9, 3] 

#random numbers will be iterated through
randomNum = 0


#clear gameOver whenever the game needs to end 
gameOver = 1

#infinite loop

while (gameOver == 1): #test if the loop needs to restart
    if randomNum > len(rowSelect):
        randomNum = 0

    #FIXME: Use a 2D list and display as a 2D list
    rowList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    columnList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    rowList.remove(rowSelect(randomNum))
    columnList.remove(rowSelect(randomNum))

    rowList.insert(randomNum, "FISH")
    columnList.insert(randomNum, "FISH")

    print(rowList) #display row and column
    print(columnList)
    print()




    print("Choose a Column: ") #temporary testing prompt

    column = input()

    print("Choose a Row: ") #temp

    row = input()

  

    randomNum = randomNum + 1
