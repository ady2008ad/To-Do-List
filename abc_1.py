import tkinter as tk

root = tk.Tk()
root.title("To Do List App")


entry = tk.Entry(root, width=40, font=("Arial", 24))
entry.grid(row=0, column=0)

tasks = []


task_frame = tk.Frame(root)
task_frame.grid(row=1, column=0, columnspan=3)

def add_task():
    current = entry.get().strip()
    if current != "":
        tasks.append(current)
        entry.delete(0, tk.END)
        show_tasks()

def delete_task(index):
    
    tasks.pop(index)
    show_tasks()

def clear_all_tasks():
    tasks.clear()
    show_tasks()

def show_tasks():
    
    for widget in task_frame.winfo_children():
        widget.destroy()
    
    for i, item in enumerate(tasks):
        task_label = tk.Label(task_frame, text=f"{i + 1}. {item}", font=("Arial", 26), anchor="w")
        task_label.grid(row=i, column=0, sticky="w")
        
        delete_btn = tk.Button(task_frame, text="Delete", command=lambda idx=i: delete_task(idx))
        delete_btn.grid(row=i, column=1, sticky="e")


tk.Button(root, text="Add Task", padx=20, pady=20, command=add_task).grid(row=0, column=1)


tk.Button(root, text="Clear All Tasks", padx=20, pady=20, command=clear_all_tasks).grid(row=0, column=2)

root.mainloop()