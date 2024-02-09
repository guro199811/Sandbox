from tkinter import *
from datetime import datetime, time

root = Tk()


root.geometry('800x400')

def timeCount():
    time = datetime.now()
    return time

starttime = timeCount()

def buttClicked():
    endtime = timeCount()
    startLabel = Label(root, text=f"Well You just Wasted {starttime - endtime} Time OF Your Life.")
    startLabel.grid(row=0, column=0)
    button = Label(root)
    button.grid(row=1, column=0)

startLabel = Label(root, text="Hiiii!!!, I Have A Present For You\n\n\n Click The Button")

button = Button(root, text='Click Me!', padx=20, pady=10, command=buttClicked,
                fg="white", bg="#283747")
button.grid(row=1, column=0)

startLabel.grid(row=0, column=0)


root.mainloop()