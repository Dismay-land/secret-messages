import random
from tkinter import simpledialog, messagebox, Tk, ttk



rps = ["rock", "paper", "scissors"]

def get_player_choice():
    player_choice = simpledialog.askstring("your choice", "Enter your choice (Rock/Paper/Scissors/exit): ").lower()
    if player_choice == 'exit':
        exit()
    return player_choice

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!",computer_choice,"vs", player_choice
    else:
        return "You lose!", computer_choice,"vs", player_choice
    
while True:
    your_choice = get_player_choice()
    computer_choice = random.choice(rps)
    winer = check_winner(your_choice, computer_choice)
    messagebox.showinfo('winer', winer)  