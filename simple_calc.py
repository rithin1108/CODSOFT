import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("400x470")
        self.root.config(bg="#2C3E50")
        self.root.resizable(False, False)
        
        self.equation = tk.StringVar()
        self.result = tk.StringVar()
        self.result.set("0")
        
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 14), borderwidth=1, relief="flat", background="#34495E", foreground="white")
        style.map('TButton', background=[('active', '#2980B9')])
        
        # Result display
        result_frame = tk.Frame(self.root, bg="#2C3E50", padx=10, pady=10)
        result_frame.pack(fill=tk.X)
        
        result_label = tk.Label(result_frame, textvariable=self.result, font=('Arial', 36), bg="#2C3E50", fg="white", anchor="e")
        result_label.pack(fill=tk.X)
        
        # Entry display
        entry_frame = tk.Frame(self.root, bg="#2C3E50", padx=10, pady=10)
        entry_frame.pack(fill=tk.X)
        
        entry = tk.Entry(entry_frame, textvariable=self.equation, font=('Arial', 24), bd=0, insertwidth=2, width=14, justify="right", bg="#34495E", fg="white")
        entry.pack(fill=tk.X, ipady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(padx=10, pady=10)
        
        buttons = [
            ('AC', 0, 0), ('⌫', 0, 1), ('^', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('√', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3),
        ]
        
        for (text, row, column) in buttons:
            self.create_button(button_frame, text, row, column)

    def create_button(self, parent, text, row, column):
        button = ttk.Button(parent, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        parent.grid_columnconfigure(column, weight=1)
        parent.grid_rowconfigure(row, weight=1)

        if text in ('AC', '⌫', '^', '/', '*', '-', '+', '=', '√'):
            button.configure(style='TButton.Special.TButton')

    def on_button_click(self, char):
        current = self.equation.get()
        
        if char == 'AC':
            self.equation.set('')
            self.result.set('0')
        elif char == '⌫':
            self.equation.set(current[:-1])
        elif char == '=':
            try:
                expression = current.replace('^', '**').replace('√', 'math.sqrt')
                result = eval(expression)
                self.result.set(f"{result:.10g}")
                self.equation.set('')
            except Exception as e:
                self.result.set('Error')
        elif char == '√':
            self.equation.set(current + '√(')
        else:
            self.equation.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()