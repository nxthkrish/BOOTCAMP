import random
import tkinter as tk
from tkinter import Label, Entry, Button

def generate_password():
    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for char in range(0, nr_letters):
        password_list += random.choice(letters)
    for char in range(0, nr_symbols):
        password_list += random.choice(symbols)

    for char in range(0, nr_numbers):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ''.join(password_list)
    result_label.config(text=f"Your generated password is: {password}")
window = tk.Tk()
window.title("Password Generator")

letter_label = Label(window, text="Letters:")
letter_label.grid(row=0, column=0)
letter_entry = Entry(window)
letter_entry.grid(row=0, column=1)

symbol_label = Label(window, text="Symbols:")
symbol_label.grid(row=1, column=0)
symbol_entry = Entry(window)
symbol_entry.grid(row=1, column=1)

number_label = Label(window, text="Numbers:")
number_label.grid(row=2, column=0)
number_entry = Entry(window)
number_entry.grid(row=2, column=1)

generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2)

result_label = Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

window.mainloop()