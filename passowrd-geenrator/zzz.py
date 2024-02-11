import random
import string
import tkinter as tk
from tkinter import Entry, Label, Button, Checkbutton, IntVar, messagebox


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_and_display(length_entry, password_entry, show_password_var):
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(show="" if show_password_var.get() else "*", state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for password length.")


def copy_to_clipboard(password_entry):
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()


def main():
    global root
    root = tk.Tk()
    root.title("Password Generator")

    Label(root, text="Password Length:").grid(row=0, column=0, pady=10)
    length_entry = Entry(root)
    length_entry.grid(row=0, column=1, pady=10)

    show_password_var = IntVar()
    Checkbutton(root, text="Show Password", variable=show_password_var).grid(row=1, column=0, columnspan=2, pady=5)

    Button(root, text="Generate Password",
           command=lambda: generate_password_and_display(length_entry, password_entry, show_password_var)).grid(row=2,
                                                                                                                column=0,
                                                                                                                columnspan=2,
                                                                                                                pady=10)

    password_entry = Entry(root, show="*")
    password_entry.grid(row=3, column=0, columnspan=2, pady=10)
    password_entry.config(state="readonly")

    Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password_entry)).grid(row=4, column=0,
                                                                                                   columnspan=2,
                                                                                                   pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
##Code-By-Fahadullah