import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # Import necessary modules from PIL

# Global variables to track scores
player_score = 0
computer_score = 0

# Global labels for score display
player_score_label = None
computer_score_label = None

def create_window():
    window = tk.Tk()
    window.title("ROCK-PAPER-SCISSORS GAME")
    window.geometry("800x600")
    window.configure(background='#4db8ff')  # Set background color

    # Load background image
    background_image = Image.open("background.jpg")
    background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(window, image=photo)
    background_label.image = photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title label
    title_label = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Helvetica", 24), bg='#4db8ff', fg='white')
    title_label.pack(pady=20)

    # "Made by:- Harsh Bhardwaj" label
    made_by_label = tk.Label(window, text="Made by:- Harsh Bhardwaj", font=("Pacifico", 12), bg='#4db8ff', fg='black')
    made_by_label.pack(pady=10)

    return window

def play_game(player_choice):
    global player_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    update_score_table()

    message = f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n{result}\n\nPlayer Score: {player_score}\nComputer Score: {computer_score}"
    messagebox.showinfo("Result", message)

    # Check if game is over (e.g., player or computer reaches 5 points)
    if player_score == 5 or computer_score == 5:
        show_final_scores()

def create_widgets(window):
    label = tk.Label(window, text="Select your move:", font=("Helvetica", 20), bg='#4db8ff', fg='white')
    label.pack(pady=10)

    button_style = {"font": ("Helvetica", 16), "padx": 30, "pady": 15, "bg": '#005580', "fg": 'white', "activebackground": '#003d4d', "activeforeground": 'white'}

    rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"), **button_style)
    rock_button.pack()

    paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"), **button_style)
    paper_button.pack()

    scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"), **button_style)
    scissors_button.pack()

    exit_button = tk.Button(window, text="Exit Game", command=window.quit, **button_style)
    exit_button.pack(pady=20)

    score_frame = tk.Frame(window, bg='#4db8ff')
    score_frame.pack(pady=20)

    tk.Label(score_frame, text="Score Table", font=("Helvetica", 18, "bold"), bg='#4db8ff', fg='white').grid(row=0, column=0, columnspan=2)

    tk.Label(score_frame, text="Player Score:", font=("Helvetica", 14), bg='#4db8ff', fg='white').grid(row=1, column=0, padx=10, pady=5)
    global player_score_label
    player_score_label = tk.Label(score_frame, text=str(player_score), font=("Helvetica", 14), bg='#4db8ff', fg='white')
    player_score_label.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(score_frame, text="Computer Score:", font=("Helvetica", 14), bg='#4db8ff', fg='white').grid(row=2, column=0, padx=10, pady=5)
    global computer_score_label
    computer_score_label = tk.Label(score_frame, text=str(computer_score), font=("Helvetica", 14), bg='#4db8ff', fg='white')
    computer_score_label.grid(row=2, column=1, padx=10, pady=5)

def update_score_table():
    global player_score, computer_score
    player_score_label.config(text=str(player_score))
    computer_score_label.config(text=str(computer_score))

def show_final_scores():
    global player_score, computer_score

    # Determine winner
    if player_score > computer_score:
        winner = "Player"
    elif computer_score > player_score:
        winner = "Computer"
    else:
        winner = "It's a tie!"

    # Construct final message
    final_message = f"Game Over!\n\nFinal Scores:\nPlayer: {player_score}\nComputer: {computer_score}\n\nWinner: {winner}"
    messagebox.showinfo("Game Over", final_message)

if __name__ == "__main__":
    window = create_window()
    create_widgets(window)
    window.mainloop()
