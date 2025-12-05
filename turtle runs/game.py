import tkinter as tk
from tkinter import messagebox

def start_game():
    messagebox.showinfo("Start Game", "Game is starting...")

def show_instructions():
    messagebox.showinfo("Instructions", "1. Do this...\n2. Do that...")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Main Menu")
root.geometry("300x200")

label = tk.Label(root, text="Main Menu", font=("Arial", 16))
label.pack(pady=20)

btn_start = tk.Button(root, text="Start Game", width=20, command=start_game)
btn_start.pack(pady=5)

btn_instructions = tk.Button(root, text="Instructions", width=20, command=show_instructions)
btn_instructions.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=20, command=exit_app)
btn_exit.pack(pady=5)

root.mainloop()