import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def get_tasks(self):
        return self.tasks

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.root.title("Vibrant To-Do List")
        self.root.geometry("550x650")
        self.root.configure(bg="#2C3E50")

        self.task_manager = task_manager

        self.create_widgets()

    def create_widgets(self):
        # Custom fonts
        title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        list_font = tkFont.Font(family="Helvetica", size=12)

        # Title Label
        self.title_label = tk.Label(self.root, text="Vibrant To-Do List", font=title_font, bg="#2C3E50", fg="#ECF0F1")
        self.title_label.pack(pady=20)

        # Task input field
        self.entry_frame = tk.Frame(self.root, bg="#2C3E50")
        self.entry_frame.pack(pady=10, padx=20, fill=tk.X)

        self.entry_task = tk.Entry(self.entry_frame, font=list_font, bg="#ECF0F1", fg="#2C3E50", insertbackground="#2C3E50")
        self.entry_task.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, 
                                    bg="#27AE60", fg="#ECF0F1", font=button_font, 
                                    activebackground="#2ECC71", activeforeground="#ECF0F1")
        self.add_button.pack(side=tk.RIGHT, padx=(10, 0))

        # Task listbox
        self.frame = tk.Frame(self.root, bg="#34495E", bd=2, relief=tk.RIDGE)
        self.frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.frame, font=list_font, bg="#ECF0F1", fg="#2C3E50", 
                                       selectbackground="#3498DB", selectforeground="#ECF0F1", 
                                       activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.button_frame = tk.Frame(self.root, bg="#2C3E50")
        self.button_frame.pack(pady=20)

        button_configs = [
            ("Mark as Done", self.mark_task_done, "#3498DB", "#2980B9"),
            ("Delete Task", self.delete_task, "#E74C3C", "#C0392B"),
            ("Exit", self.root.quit, "#95A5A6", "#7F8C8D")
        ]

        for text, command, bg, active_bg in button_configs:
            button = tk.Button(self.button_frame, text=text, command=command, 
                               bg=bg, fg="#ECF0F1", font=button_font, 
                               activebackground=active_bg, activeforeground="#ECF0F1")
            button.pack(side=tk.LEFT, padx=5)

        self.update_task_listbox()

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark_task_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            if self.task_manager.mark_task_done(selected_task_index):
                self.update_task_listbox()
                messagebox.showinfo("Success", "Task marked as done!")
            else:
                messagebox.showwarning("Warning", "Invalid task number!")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            select_task_index = self.task_listbox.curselection()[0]
            if self.task_manager.delete_task(select_task_index):
                self.update_task_listbox()
                messagebox.showinfo("Success", "Task deleted!")
            else:
                messagebox.showwarning("Warning", "Invalid task number!")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.task_manager.get_tasks()):
            status = "✅" if task["done"] else "⏳"
            self.task_listbox.insert(tk.END, f"{index + 1}. {status} {task['task']}")
            if task["done"]:
                self.task_listbox.itemconfig(index, fg="grey")

if __name__ == "__main__":
    task_manager = TaskManager()
    root = tk.Tk()
    app = ToDoApp(root, task_manager)
    root.mainloop()