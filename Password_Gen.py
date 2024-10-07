import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x600")  # Increased window size
        self.root.resizable(False, False)

        # Updated color scheme
        self.bg_color = "#2C3E50"  # Dark blue-gray
        self.title_color = "#E74C3C"  # Bright red
        self.label_color = "#ECF0F1"  # Off-white
        self.btn_color = "#3498DB"  # Bright blue
        self.entry_bg_color = "#34495E"  # Darker blue-gray
        self.entry_fg_color = "#FFFFFF"  # White
        self.radio_bg_color = "#34495E"  # Darker blue-gray
        self.radio_select_color = "#2980B9"  # Slightly lighter blue
        self.password_fg_color = "#2ECC71"  # Bright green

        self.root.config(bg=self.bg_color)

        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), bg=self.bg_color,
                                    fg=self.title_color)
        self.title_label.pack(pady=30)

        self.length_label = tk.Label(root, text="Enter the desired length of the password:", font=("Helvetica", 14),
                                     bg=self.bg_color, fg=self.label_color)
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Helvetica", 14), width=7, bg=self.entry_bg_color,
                                     fg=self.entry_fg_color, insertbackground=self.entry_fg_color)
        self.length_entry.pack(pady=10)

        self.strength_title_label = tk.Label(root, text="Password Strength:", font=("Helvetica", 14, "bold"),
                                             bg=self.bg_color, fg=self.label_color)
        self.strength_title_label.pack(pady=20)

        self.strength_frame = tk.Frame(root, bg=self.bg_color)
        self.strength_frame.pack(pady=10)

        self.strength_var = tk.StringVar(value="easy")

        self.easy_radio = tk.Radiobutton(self.strength_frame, text="Easy", variable=self.strength_var, value="easy",
                                         font=("Helvetica", 14), bg=self.radio_bg_color, fg=self.label_color,
                                         selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.easy_radio.grid(row=0, column=0, padx=15)

        self.moderate_radio = tk.Radiobutton(self.strength_frame, text="Moderate", variable=self.strength_var,
                                             value="moderate", font=("Helvetica", 14), bg=self.radio_bg_color,
                                             fg=self.label_color, selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.moderate_radio.grid(row=0, column=1, padx=15)

        self.hard_radio = tk.Radiobutton(self.strength_frame, text="Hard", variable=self.strength_var, value="hard",
                                         font=("Helvetica", 14), bg=self.radio_bg_color, fg=self.label_color,
                                         selectcolor=self.radio_select_color, activebackground=self.bg_color)
        self.hard_radio.grid(row=0, column=2, padx=15)

        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 14, "bold"),
                                         bg=self.btn_color, fg=self.label_color, command=self.generate_password,
                                         activebackground="#2980B9", activeforeground=self.label_color)
        self.generate_button.pack(pady=20)

        self.clear_button = tk.Button(root, text="Clear", font=("Helvetica", 14, "bold"), bg=self.btn_color,
                                      fg=self.label_color, command=self.clear_password,
                                      activebackground="#2980B9", activeforeground=self.label_color)
        self.clear_button.pack(pady=10)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg=self.bg_color,
                                       fg=self.password_fg_color, wraplength=450)
        self.password_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1!")

            strength = self.strength_var.get()

            if strength == "easy":
                characters = string.ascii_lowercase
            elif strength == "moderate":
                characters = string.ascii_letters + string.digits
            else:
                characters = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))

            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def clear_password(self):
        self.password_label.config(text="")
        self.length_entry.delete(0, tk.END)
        self.strength_var.set("easy")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()