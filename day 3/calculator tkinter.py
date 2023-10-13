import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def equals():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    if math == "division":
        entry.insert(0, f_num / float(second_number))

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field for input
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", command=lambda: button_click(0))

# Create operator buttons
button_add = tk.Button(window, text="+", command=add)
button_subtract = tk.Button(window, text="-", command=subtract)
button_multiply = tk.Button(window, text="*", command=multiply)
button_divide = tk.Button(window, text="/", command=divide)
button_equal = tk.Button(window, text="=", command=equals)
button_clear = tk.Button(window, text="C", command=clear)

# Place buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

# Run the Tkinter main loop
window.mainloop()