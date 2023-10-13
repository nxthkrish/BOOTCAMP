import tkinter as tk

# Function to update the label text
def update_label():
    num = float(entry.get())
    square=num**2
    label.config(text=f"the square of {num} is {square}")

root = tk.Tk()
root.title("Text Entry and Display")
# Create an Entry widget for text input
entry = tk.Entry(root)
entry.pack(pady=100)

# Create a button to trigger the label update
update_button = tk.Button(root, text="SUBMIT", command=update_label)
update_button.pack()

# Create a Label widget to display the entered text
label = tk.Label(root, text="", pady=100)
label.pack()

# Start the Tkinter main loop
root.mainloop()