import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button clicks
def play_game():
    user_choice = user_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create a label for instructions
instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instructions_label.pack()

# Create radio buttons for user's choice
user_var = tk.StringVar()
rock_button = tk.Radiobutton(root, text="Rock", variable=user_var, value="rock")
paper_button = tk.Radiobutton(root, text="Paper", variable=user_var, value="paper")
scissors_button = tk.Radiobutton(root, text="Scissors", variable=user_var, value="scissors")
rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create a button to play the game
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
