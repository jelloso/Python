#Dodge the bombs program code from page 62-64.
#This version allows you to test the code so far.
#It will create a blank tkinter window and print out a grid of 0s and 1s in the Shell.
#It also creates an error message.
#This is because you haven't defined the layout_window() function yet.

#1

import tkinter
import random

#2

gameOver = False
score = 0
squaresToClear = 0

#3
def play_bombdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()

#p63, #4

bombfield = []

def create_bombfield(bombfield):
    global squaresToClear
#5
    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) <20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
        bombfield.append(rowList)
        
#page64, step 6
    printfield(bombfield)

def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

play_bombdodger()
        



