import tkinter as tk
from tkinter import messagebox
import json

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please fill in all the fields.")

def search_password():
    website = website_entry.get()
    if website:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    username = data[website]["username"]
                    password = data[website]["password"]
                    messagebox.showinfo(website, f"Username: {username}\nPassword: {password}")
                else:
                    messagebox.showinfo("Info", f"No details for {website} exists.")
        except FileNotFoundError:
            messagebox.showinfo("Info", "No Data File Found.")
    else:
        messagebox.showwarning("Warning", "Please enter a website name.")

window = tk.Tk()
window.title("Password Manager")

website_label = tk.Label(text="Website:")
website_label.grid(row=0, column=0)
website_entry = tk.Entry(width=21)
website_entry.grid(row=0, column=1)
website_entry.focus()

username_label = tk.Label(text="Username/Email:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(width=40)
username_entry.grid(row=1, column=1, columnspan=2)

password_label = tk.Label(text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=2, column=1)

add_button = tk.Button(text="Add", width=36, command=add_password)
add_button.grid(row=3, column=1, columnspan=2)

search_button = tk.Button(text="Search", width=13, command=search_password)
search_button.grid(row=0, column=2)

window.mainloop()
