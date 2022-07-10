#Weakest Link by James Mann

#Defines all of the imports needed
from tkinter import *
import tkinter.font as font
import json
import random

#Window Setup
root=Tk()
root.title("Weakest Link")
root.resizable(False,False)

global index
global scoreArray
global currentTotal
global currentPlayer
global playerArray
global questions
global runningLabel
global currentLabel
global currentPlayerLabel
global qAndALabel
global categoryLabel
global bankButton

index = 0
scoreArray = [0, 20, 50, 100, 200, 400, 600, 800, 1000]
currentTotal = 0
currentPlayer = 0

buttonFont = font.Font(family="Neusa Next", size = 45, underline = 1)
endFont = font.Font(family="Neusa Next", size = 18)
textFont = font.Font(family="Neusa Next", size = 22)
questionFont = font.Font(family="Neusa Next", size = 16)

class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.banks = 0

def correct():
    global index
    global currentPlayer
    
    if index < len(scoreArray) - 1:
        index += 1
        runningLabel.config(text = "Money: "+str(scoreArray[index]))
    else:
        bank()
        index += 1
        runningLabel.config(text = "Money: "+str(scoreArray[index]))
    
    playerArray[currentPlayer%len(playerArray)].correct += 1
    
    updateCurrentPlayer()
        
def incorrect():
    global index
    global currentPlayer
    global questions
    
    index = 0
    runningLabel.config(text = "Money: "+str(0))
    
    updateCurrentPlayer()

def bank():
    global index
    global currentTotal
    global currentPlayer
    
    currentTotal += scoreArray[index]
    index = 0
    runningLabel.config(text =  "Money: "+str(0))
    currentLabel.config(text =  "Total: "+str(currentTotal))
 
    playerArray[currentPlayer%len(playerArray)].banks += 1
    
    setBank()
    
def updateCurrentPlayer():
    global currentPlayer
    global questions
    
    currentPlayer += 1
    currentPlayerLabel.config(text = str(playerArray[currentPlayer%len(playerArray)].name))
    
    if (len(questions) == 0):
        print("\nResetting and repeating questions")
        file = open("trivia.json")
        questions = json.load(file)
        file.close()
        
    setBank()    
    reroll()

def reset():
    global playerArray
    playerArray = []
    file = open("players.txt","r")
    text = file.read()
    playerNameArray = text.split(", ")
    file.close()
    
    i = 0
    for i in range(0,len(playerNameArray)):
        playerArray.append(Player(playerNameArray[i]))
    
    endRound()

def endRound():
    global playerArray
    global currentPlayer
    global index
    global questions 
    
    index = 0
    setBank()
    runningLabel.config(text = "Money: "+str(scoreArray[index]))
    
    print("\nID\tName\t\tCorrect\tBanks")
    print("-------------------------------------")
    for i in range (0,len(playerArray)):
        player = playerArray[i]
        print(f"{i}\t{player.name}\t\t{player.correct}\t{player.banks}")
        player.correct = 0
        player.banks = 0
    
    while (True):    
        playerRemoved = int(input("\nID of the weakest link (chosen by players): "))
        if playerRemoved == -1:
            print("Aborted")
            break
        elif 0 <= playerRemoved < len(playerArray):
            print(f"Removed {playerArray[playerRemoved].name}")
            break
        else:
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
    
    currentPlayerLabel.config(text = str(playerArray[currentPlayer%len(playerArray)].name))
    
    setBank()
    reroll()

def reroll():
    global currentPlayer
    global questions
    
    if (len(questions) == 0):
        print("\nResetting and repeating questions")
        file = open("trivia.json")
        questions = json.load(file)
        file.close()
        
    q = random.choice(questions)
    questions.remove(q)
    
    categoryLabel.config(text=q["category"])
    qAndALabel.config(text="Q: "+q["question"]+"\nA: "+q["answer"])

def setBank():
    if index == 0: bankButton.config(state=DISABLED)   
    else: bankButton.config(state=NORMAL) 

playerArray = []
file = open("players.txt","r")
text = file.read()
playerNameArray = text.split(", ")
file.close()

i = 0
for i in range(0,len(playerNameArray)):
    playerArray.append(Player(playerNameArray[i]))

file = open("trivia.json")
questions = json.load(file)
q = random.choice(questions)
questions.remove(q)
file.close()

#Buttons that the player uses
correctButton=Button(root, text="Correct", command=correct, bg="#81c97b", font = buttonFont, width = 11).grid(row=0, column=0)
incorrectButton=Button(root, text="Incorrect", command=incorrect, bg="#cf4a55", font = buttonFont, width = 11).grid(row=0, column=1)
endRoundButton=Button(root, text="End Round", command=endRound, bg="#fff3cf", font = endFont).grid(row=1, column=2)
redoButton=Button(root, text="Reroll Question", command=reroll, bg="#8adcff", font = endFont).grid(row=3, column=1)
resetButton=Button(root, text="Reset Game", command=reset, bg="#ff9ef7", font = endFont).grid(row=4, column=0)

bankButton=Button(root, text="Bank", command=bank, bg="#61a2c7", font = buttonFont, width = 11, state=DISABLED)
bankButton.grid(row=0, column=2)

runningLabel=Label(root, text = "Money: "+str(scoreArray[index]), font=textFont)
runningLabel.grid(row=3, column=0)
currentLabel=Label(root, text = "Total: "+str(currentTotal), font=textFont)
currentLabel.grid(row=3, column=2)
qAndALabel=Label(root, text ="Q: "+q["question"]+"\nA: "+q["answer"], font=questionFont)
qAndALabel.grid(row=2, columnspan=3)
categoryLabel=Label(root, text =q["category"], font=textFont)
categoryLabel.grid(row=1, column =1)
currentPlayerLabel=Label(root, text = str(playerArray[currentPlayer].name), font = textFont)
currentPlayerLabel.grid(row=1, column=0)

#Runs the game
root.mainloop()