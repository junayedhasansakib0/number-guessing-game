import random
import tkinter as tk
from tkinter import simpledialog,messagebox

print("\n ----Number Guessing Game----")

# Create the GUI application window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Welcome Message
messagebox.showinfo("Number Guessing Game", "Welcome to the Number Guessing Game!")


# Generate a random number between 1 and 20 (inclusive)
secret_number = random.randint(1, 20)
guessed_numbers = [] # Renamed for clarity
last_user_guess = None
consecutive_duplicate_count= 0
def play_game():
    chance_limit = 0
    global last_user_guess
    global consecutive_duplicate_count
    # Loop to ensure a positive chance_limit is entered
    while chance_limit <= 0:
        try:
            chance_limit = int(input("How many times do you want to guess the number?: "))
            if chance_limit <= 0:
                print("Please enter a positive number of chances. Try again.")
                messagebox.showerror("Please enter a positive number of chances. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer for the number of chances. Try again.")
            messagebox.showerror("Invalid input. Please enter an integer for the number of chances. Try again.")

    current_chance = 0

    while current_chance < chance_limit:
        print(f"\n--- Chance {current_chance + 1} of {chance_limit} ---")
        try:
            user_guess = int(input("Enter a number between 1 and 20: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue # Skip to the next iteration if input is not an integer

        if user_guess < 1 or user_guess > 20:
            print("Your guess is out of the 1 to 20 range. Please try again.")
            continue # Skip to the next iteration if guess is out of range


        if user_guess == last_user_guess:
            consecutive_duplicate_count += 1
            print(f"You guessed {user_guess} consecutively {consecutive_duplicate_count} time(s).")
            if consecutive_duplicate_count >= 3:
                print(f"You have guessed the number {user_guess} consecutively 3 times!")
                print("You are out from this game for guessing the same number repeatedly!")
                break
            else:
                last_user_guess = user_guess
                consecutive_duplicate_count = 0



        if user_guess in guessed_numbers:
            print(f"You have already guessed the number {user_guess} before.")
            # Decrement chance_limit instead of current_chance to reflect loss of a "life"
            chance_limit -= 1
            print(f"You lost one chance for guessing a duplicate. Remaining chances: {chance_limit}")
            # The current_chance is NOT incremented, so the user gets to replay this chance
            if chance_limit <= 0: # Check if all chances are lost due to duplicates
                print("You've run out of chances due to duplicate guesses.")
                print(f"The correct number was {secret_number}.")
                break # End the game
            continue # Continue to the next iteration of the while loop, effectively replaying the chance
        else:
            guessed_numbers.append(user_guess) # Add the new guess to the list

            if user_guess == secret_number:
                print(f"Correct! You have guessed the number {secret_number}.")
                print(f"It took you {current_chance + 1} attempts.")
                break # End the game if the number is guessed
            else:
                print("Incorrect!")
                # Only increment current_chance if the guess was new and incorrect
                current_chance += 1
                if current_chance == chance_limit: # Last chance
                    print(f"You've run out of chances. Your guesses were: {guessed_numbers}")
                    print(f"The correct number was {secret_number}.")
    else: # This 'else' block executes if the while loop completes without a 'break'
        if current_chance == chance_limit and user_guess != secret_number: # Only print if the last guess was incorrect
             print("\nGame Over! You didn't guess the number in time.")


try:
    play_game()
except Exception as e:
    print(f"An unexpected error occurred: {e}")