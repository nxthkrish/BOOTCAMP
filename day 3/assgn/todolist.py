import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def mark_completed():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, {'bg': 'light green'})

window = tk.Tk()
window.title("To-Do List")

entry = tk.Entry(window, width=30)
entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
remove_button = tk.Button(window, text="Remove Task", command=remove_task)
complete_button = tk.Button(window, text="Mark Completed", command=mark_completed)

add_button.pack()
remove_button.pack()
complete_button.pack()

task_list = tk.Listbox(window, selectmode=tk.SINGLE)
task_list.pack()

window.mainloop()