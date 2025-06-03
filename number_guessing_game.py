import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import sys
import os

# Game variables
secret_number = random.randint(1, 20)
guessed_numbers = []
last_user_guess = None
consecutive_duplicate_count = 0
chance_limit = 0
current_chance = 0
game_history = []

# Functions
def submit_chance():
    global chance_limit
    try:
        val = int(chance_entry.get())
        if val <= 0:
            chat_area.insert(tk.END, "Enter a positive number of chances.\n", "error")
        elif val > 10:
            chat_area.insert(tk.END, "Maximum 10 chances allowed.\n", "error")
        else:
            chance_limit = val
            chance_entry.config(state="disabled")
            chance_button.config(state="disabled")
            guess_entry.config(state="normal")
            guess_button.config(state="normal")
            chat_area.insert(tk.END, f"You have {chance_limit} chances to guess the number between 1 and 20.\n", "info")
            chat_area.see(tk.END)
    except ValueError:
        chat_area.insert(tk.END, "Invalid input. Please enter a number.\n", "error")
        chat_area.see(tk.END)

def process_guess():
    global last_user_guess, consecutive_duplicate_count, current_chance, chance_limit
    if chance_limit <= 0:
        chat_area.insert(tk.END, "Please enter the number of chances first.\n", "error")
        chat_area.see(tk.END)
        return

    user_input = guess_entry.get()
    guess_entry.delete(0, tk.END)

    try:
        user_guess = int(user_input)
    except ValueError:
        chat_area.insert(tk.END, "Invalid input. Please enter a number.\n", "error")
        chat_area.see(tk.END)
        return

    if user_guess < 1 or user_guess > 20:
        chat_area.insert(tk.END, "Out of range. Please guess between 1 and 20.\n", "error")
        chat_area.see(tk.END)
        return

    if user_guess == last_user_guess:
        consecutive_duplicate_count += 1
        chat_area.insert(tk.END, f"You guessed {user_guess} again ({consecutive_duplicate_count} times in a row).\n", "warning")
        if consecutive_duplicate_count >= 3:
            chat_area.insert(tk.END, "Guessed same number 3 times in a row. Game Over!\n", "error")
            disable_input()
            show_guess_history()
            return
    else:
        last_user_guess = user_guess
        consecutive_duplicate_count = 1

    if user_guess in guessed_numbers:
        chance_limit -= 1
        chat_area.insert(tk.END, f"Duplicate guess! You lost one chance. Remaining: {chance_limit}\n", "warning")
        if chance_limit <= 0:
            chat_area.insert(tk.END, f"No chances left. The number was {secret_number}\n", "error")
            disable_input()
            show_guess_history()
        chat_area.see(tk.END)
        return
    else:
        guessed_numbers.append(user_guess)
        game_history.append(user_guess)

    if user_guess == secret_number:
        chat_area.insert(tk.END, f"🎉 Correct! The number was {secret_number}. You guessed it in {current_chance + 1} tries.\n", "success")
        disable_input()
        show_guess_history()
    else:
        hint = "Too low!" if user_guess < secret_number else "Too high!"
        chat_area.insert(tk.END, f"❌ Incorrect guess. {hint}\n", "warning")
        current_chance += 1
        if current_chance >= chance_limit:
            chat_area.insert(tk.END, f"Game Over! You've used all your chances.\nThe number was {secret_number}.\n", "error")
            disable_input()
            show_guess_history()
    chat_area.see(tk.END)

def disable_input():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")
    restart_button.config(state="normal")

def restart_game():
    global secret_number, guessed_numbers, last_user_guess, consecutive_duplicate_count, chance_limit, current_chance, game_history
    secret_number = random.randint(1, 20)
    guessed_numbers = []
    last_user_guess = None
    consecutive_duplicate_count = 0
    chance_limit = 0
    current_chance = 0
    game_history = []
    chance_entry.config(state="normal")
    chance_button.config(state="normal")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    restart_button.config(state="disabled")
    chat_area.delete(1.0, tk.END)
    chat_area.insert(tk.END, "🎮 Welcome to the Number Guessing Game!\nGuess a number between 1 and 20.\n\n", "info")
    chance_entry.delete(0, tk.END)
    chat_area.see(tk.END)

def show_guess_history():
    if not game_history:
        return
    chat_area.insert(tk.END, "\nGuess History:\n", "info")
    for i, guess in enumerate(game_history, 1):
        chat_area.insert(tk.END, f"Guess {i}: {guess}\n", "info")
    chat_area.insert(tk.END, f"Secret Number: {secret_number}\n", "success")
    chat_area.see(tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="#e0e7ff")  # Soft indigo background
root.geometry("600x650")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# Set application icon (if available)
try:
    icon_path = os.path.join(os.path.dirname(sys.executable), "icon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
except:
    pass

# Styling
font_style = ("Helvetica", 12, "normal")
title_font = ("Helvetica", 16, "bold")
button_style = {"bg": "#6366f1", "fg": "white", "font": font_style, "activebackground": "#4f46e5", "relief": "flat", "padx": 10, "pady": 5}
entry_style = {"font": font_style, "bg": "#ffffff", "bd": 2, "relief": "groove"}
label_style = {"font": font_style, "bg": "#e0e7ff", "fg": "#1f2937"}

# Title
title_label = tk.Label(root, text="Number Guessing Game", font=title_font, bg="#e0e7ff", fg="#1f2937")
title_label.pack(pady=10)

# Chat area with tags for colored text
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state="normal", font=font_style, bg="#ffffff", bd=2, relief="groove")
chat_area.insert(tk.END, "🎮 Welcome to the Number Guessing Game!\nGuess a number between 1 and 20.\n\n", "info")
chat_area.pack(padx=20, pady=10)
chat_area.tag_config("error", foreground="#dc2626")  # Red for errors
chat_area.tag_config("warning", foreground="#d97706")  # Amber for warnings
chat_area.tag_config("success", foreground="#15803d")  # Green for success
chat_area.tag_config("info", foreground="#1f2937")  # Dark gray for info

# Chance input
chance_frame = tk.Frame(root, bg="#e0e7ff")
chance_label = tk.Label(chance_frame, text="Number of Chances (1-10):", **label_style)
chance_label.pack(side=tk.LEFT)
chance_entry = tk.Entry(chance_frame, width=10, **entry_style)
chance_entry.pack(side=tk.LEFT, padx=10)
chance_button = tk.Button(chance_frame, text="Set", command=submit_chance, **button_style)
chance_button.pack(side=tk.LEFT)
chance_frame.pack(pady=10)

# Guess input
guess_frame = tk.Frame(root, bg="#e0e7ff")
guess_label = tk.Label(guess_frame, text="Your Guess:", **label_style)
guess_label.pack(side=tk.LEFT)
guess_entry = tk.Entry(guess_frame, width=30, **entry_style)
guess_entry.pack(side=tk.LEFT, padx=10)
guess_button = tk.Button(guess_frame, text="Guess", command=process_guess, **button_style)
guess_button.pack(side=tk.LEFT)
guess_frame.pack(pady=10)

# Restart button
restart_button = tk.Button(root, text="Restart Game", command=restart_game, **button_style, state="disabled")
restart_button.pack(pady=10)

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_closing)

# Focus on guess entry when pressing Enter
root.bind('<Return>', lambda event: process_guess())

# Start GUI loop
root.mainloop()