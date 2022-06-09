#Blackjack by James Mann

#Defines all of the imports needed
from tkinter import *
import tkinter
import tkinter.font as font
import time

#Window Setup
root=Tk()
root.title("Weakest Link")
root.resizable(False,False)

global index
global scoreArray
global currentTotal
global currentPlayer
global playerArray

index = 0
scoreArray = [0, 20, 50, 100, 200, 400, 600, 800, 1000]
currentTotal = 0
currentPlayer = 0

buttonFont = font.Font(family="Neusa Next", size = 30, underline = 1)
endFont = font.Font(family="Neusa Next", size = 15)
textFont = font.Font(family="Neusa Next", size = 15)

class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.banks = 0

def correct():
    global index
    global playerArray
    global currentPlayer
    
    if index < len(scoreArray) - 1:
        index += 1
        runningLabel = Label(root, text = "                      ", font=textFont).grid(row=1, column=0)
        runningLabel = Label(root, text = "Money: "+str(scoreArray[index]), font=textFont).grid(row=1, column=0)
    else:
        bank()
        index += 1
        runningLabel = Label(root, text = "                      ", font=textFont).grid(row=1, column=0)
        runningLabel = Label(root, text = "Money: "+str(scoreArray[index]), font=textFont).grid(row=1, column=0)
    
    playerArray[currentPlayer%len(playerArray)].correct += 1
        
    updateCurrentPlayer()
        
def incorrect():
    global index
    global playerArray
    global currentPlayer
    index = 0
    runningLabel = Label(root, text = "                      ", font=textFont).grid(row=1, column=0)
    runningLabel = Label(root, text = "Money: "+str(0), font=textFont).grid(row=1, column=0)
    updateCurrentPlayer()

def bank():
    global index
    global currentTotal
    global playerArray
    global currentPlayer
    
    currentTotal += scoreArray[index]
    index = 0
    runningLabel = Label(root, text = "                      ", font=textFont).grid(row=1, column=0)
    runningLabel = Label(root, text =  "Money: "+str(0), font=textFont).grid(row=1, column=0)
    currentLabel = Label(root, text =  "Total: "+str(currentTotal), font=textFont).grid(row=1, column=2)
 
    playerArray[currentPlayer%len(playerArray)].banks += 1
    
def updateCurrentPlayer():
    global currentPlayer
    currentPlayer += 1
    currentPlayerLabel = Label(root, text = "                 ", font = textFont).grid(row=2, column=0)
    currentPlayerLabel = Label(root, text = str(playerArray[currentPlayer%len(playerArray)].name), font = textFont).grid(row=2, column=0)
    
def endRound():
    global playerArray
    global currentPlayer
    global index
    
    index = 0
    runningLabel = Label(root, text = "                 ", font=textFont).grid(row=1, column=0)
    runningLabel = Label(root, text = "Money: "+str(scoreArray[index]), font=textFont).grid(row=1, column=0)
    
    print("\nID\tName\t\tCorrect\tBanks")
    print("-------------------------------------")
    for i in range (0,len(playerArray)):
        player = playerArray[i]
        print(f"{i}\t{player.name}\t\t{player.correct}\t{player.banks}")
        player.correct = 0
        player.banks = 0
    
    while (True):    
        playerRemoved = int(input("\nID of the weakest link (chosen by players): "))
        if 0 <= playerRemoved < len(playerArray):
            print(f"Removed {playerArray[playerRemoved].name}")
            break
        print("Invalid player")
    
    while (True):    
        currentPlayer = int(input("\nID of the strongest link: "))
        if currentPlayer == playerRemoved:
            print("The strongest link cannot be the weakest link")
            
        elif 0 <= currentPlayer < len(playerArray):
            print(f"The strongest link was {playerArray[currentPlayer].name}")
            break
        
        else:
            print("Invalid player")
    
    
    if playerRemoved < currentPlayer:
        currentPlayer -= 1
    
    playerArray.remove(playerArray[playerRemoved])

    currentPlayerLabel = Label(root, text = "         ", font = textFont).grid(row=2, column=0)
    currentPlayerLabel = Label(root, text = str(playerArray[currentPlayer%len(playerArray)].name), font = textFont).grid(row=2, column=0)
        

playerArray = []
file = open("players.txt","r")
text = file.read()
playerNameArray = text.split(", ")
file.close()

i = 0
for i in range(0,len(playerNameArray)):
    playerArray.append(Player(playerNameArray[i]))

#Buttons that the player uses
correctButton=Button(root, text="Correct", command=correct, bg="#81c97b", font = buttonFont).grid(row=0, column=0)
incorrectButton=Button(root, text="Incorrect", command=incorrect, bg="#cf4a55", font = buttonFont).grid(row=0, column=1)
bankButton=Button(root, text="Bank", command=bank, bg="#61a2c7", font = buttonFont).grid(row=0, column=2)
runningLabel = Label(root, text = "Money: "+str(scoreArray[index]), font=textFont).grid(row=1, column=0)
currentLabel = Label(root, text = "Total: "+str(currentTotal), font=textFont).grid(row=1, column=2)
endRoundButton=Button(root, text="End Round", command=endRound, bg="#fff3cf", font = endFont).grid(row=2, column=2)
currentPlayerLabel = Label(root, text = str(playerArray[currentPlayer].name), font = textFont).grid(row=2, column=0)

#Runs the game
root.mainloop()