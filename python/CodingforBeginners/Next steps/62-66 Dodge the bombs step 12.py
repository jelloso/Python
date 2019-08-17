#This is the dodge the bombs game up to page 66, step 12.
#It creates the field but you can't click on it yet.

#page 62

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

#step7
def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

#step 9

def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
#step 10 (page 65)
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg= "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg= "seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg= "green")
#step 11
            square.grid(row = rowNumber, column = columnNumber)

#step 12 (page 66)
play_bombdodger()
