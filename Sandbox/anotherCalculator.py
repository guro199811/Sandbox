from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('375x600')  # Set the size of the window

# Create an entry widget for the display
display = Entry(root, width=14, borderwidth=5, font=("Helvetica", 32), bg='black', fg='white')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click event
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, END)

def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0, END)
    if math == "addition":
        display.insert(0, f_num + int(second_number))

# Define your buttons
buttons = [
    '(', ')', 'mod', 'n',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '%', '+'
]

# Create and place buttons on the grid
for i in range(5):
    for j in range(4):
        if buttons[i*4+j] in '0123456789':
            button = Button(root, text=buttons[i*4+j], padx=20, pady=20, bg='grey', fg='white', activebackground='darkgrey', command=lambda x=buttons[i*4+j]: button_click(int(x)))
        elif buttons[i*4+j] == '+':
            button = Button(root, text=buttons[i*4+j], padx=20, pady=20, bg='grey', fg='white', activebackground='darkgrey', command=button_add)
        elif buttons[i*4+j] == '=':
            button = Button(root, text=buttons[i*4+j], padx=20, pady=20, bg='grey', fg='white', activebackground='darkgrey', command=button_equal)
        else:
            button = Button(root, text=buttons[i*4+j], padx=20, pady=20, bg='grey', fg='white', activebackground='darkgrey')
        button.grid(row=i+1, column=j)

# Run the application
root.mainloop()
