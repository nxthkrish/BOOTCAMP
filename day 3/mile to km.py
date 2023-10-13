import tkinter as tk
def mlkm():
    miles=float(entry_miles.get())
    kilometres=miles * 1.60934
    label_result.config(text=f"{miles} miles is equal to {kilometres:.2f} kilometers")
root=tk.Tk()
root.title("Miles to kilometer converter")
label_miles = tk.Label(root, text="Enter Miles:")
label_miles.grid(row=0, column=0)
entry_miles = tk.Entry(root)
entry_miles.grid(row=0, column=1)
label_result = tk.Label(root, text="")
label_result.grid(row=1, column=0, columnspan=2)
convert_button = tk.Button(root, text="Convert", command=mlkm)
convert_button.grid(row=2, column=0, columnspan=2)
root.mainloop()


    