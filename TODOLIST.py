import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.config(bg="#2b2b2b")

        self.tasks = []

        
        self.title_label = tk.Label(self.root, text="My To-Do List", bg="#2b2b2b", fg="white", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        
        self.tasks_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.tasks_frame.pack()

        
        self.tasks_listbox = tk.Listbox(
            self.tasks_frame, height=15, width=50, selectmode=tk.SINGLE,
            bg="#3c3f41", fg="white", font=("Helvetica", 12), bd=0, highlightthickness=0,
            selectbackground="#6a9fb5", selectforeground="black"
        )
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

       
        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        
        self.task_entry = tk.Entry(self.root, width=50, bg="#3c3f41", fg="white", font=("Helvetica", 12), bd=0)
        self.task_entry.pack(pady=10)

        
        self.add_button = tk.Button(
            self.root, text="Add Task", width=42, command=self.add_task,
            bg="#6a9fb5", fg="black", font=("Helvetica", 12), bd=0, highlightthickness=0
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            self.root, text="Delete Task", width=42, command=self.delete_task,
            bg="#ff4b5c", fg="black", font=("Helvetica", 12), bd=0, highlightthickness=0
        )
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
