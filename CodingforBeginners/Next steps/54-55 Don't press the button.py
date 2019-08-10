#Don't press the button
#pp54-55


import tkinter
window = tkinter.Tk()
#you can save and run after typing the above, to get a blank GUI window

button = tkinter.Button(window, text="Do not press this button.", width=40)
button.pack(padx=10, pady=10)
#save and run the code above to see a button with text on

clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickCount == 2:
        button.configure(text="Gah! Next time, no more button.")
    else:
        button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
