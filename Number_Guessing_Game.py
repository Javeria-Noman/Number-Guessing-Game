
import tkinter as tk
import random

# Generate secret number
secret_number = random.randint(1, 10)

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")
root.config(bg="#202A44")

# Heading
title = tk.Label(
    root,
    text="Number Guessing Game",
    font=("Arial", 20, "bold"),
    bg="#202A44",
    fg="white"
)
title.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Guess a number between 1 and 10",
    font=("Arial", 12),
    bg="#202A44",
    fg="white"
)
instruction.pack(pady=10)

# Input box
guess_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
guess_entry.pack(pady=10)


# Check guess function
def check_guess():
    guess = guess_entry.get()

    if not guess.isdigit():
        result_label.config(text="Please enter a valid number!")
        return

    guess = int(guess)

    if guess < 1 or guess > 10:
        result_label.config(text="Enter number between 1 and 10!")

    elif guess == secret_number:
        result_label.config(
            text="Congratulations! You Won!",
            fg="lightgreen"
        )

    elif guess > secret_number:
        result_label.config(
            text="Too High! Try Again.",
            fg="orange"
        )

    else:
        result_label.config(
            text="Too Low! Try Again.",
            fg="orange"
        )


# Guess button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    command=check_guess,
    bg="#4CAF50",
    fg="white"
)
guess_button.pack(pady=10)

# Result message
result_label = tk.Label(
    root,
    text="Good Luck!",
    font=("Arial", 12, "bold"),
    bg="#202A44",
    fg="white"
)
result_label.pack(pady=15)


# Restart function
def restart_game():
    global secret_number
    secret_number = random.randint(1, 10)
    guess_entry.delete(0, tk.END)
    result_label.config(text="New Game! Good Luck!", fg="white")


# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 11),
    command=restart_game
)
restart_button.pack(pady=5)

# Run application
root.mainloop()
