#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator, from Gs")
root.geometry("800x400")

style = ttk.Style()
style.configure('TButton', background='black', foreground='white', font=("default", 20))

calc_input = tk.StringVar()


frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

input_entry = tk.Entry(frame, textvariable=calc_input, font=("default", 20), justify='right')
input_entry.grid(row=0, column=0, columnspan=4)

def number(num):
    calc_input.set(calc_input.get() + str(num))

def clear():
    calc_input.set('')

def calculate():
    try:
        calc_input.set(str(eval(calc_input.get())))
    except Exception as e:
        print(e)
        calc_input.set("Error")

for i in range(1, 10):
    button = ttk.Button(frame, text=str(i), style='TButton', command=lambda i=i: number(i))
    button.grid(row=(i-1)//3+1, column=(i-1)%3, padx=5, pady=5)

for i, op in enumerate(['+', '-', '*', '/']):
    button = ttk.Button(frame, text=op, style='TButton',  command=lambda op=op: number(op))
    button.grid(row=i+1, column=3, padx=5, pady=5)

button = ttk.Button(frame, text='C', style='TButton', command=clear)
button.grid(row=4, column=0, padx=5, pady=5)

button = ttk.Button(frame, text='=', style='TButton', command=calculate)
button.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky='we')

root.mainloop()
