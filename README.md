# Number Guessing Game

## Overview
This is a simple command-line **Number Guessing Game** implemented in Python. The player tries to guess a randomly generated number between 1 and 20 within a specified number of attempts. The game includes features to handle duplicate guesses, consecutive identical guesses, and invalid inputs, making it both challenging and user-friendly.

## Features
- **Random Number Generation**: The game generates a random number between 1 and 20 using Python's `random` module.
- **Customizable Attempts**: Players can specify how many chances they want to guess the number.
- **Input Validation**: Ensures guesses are valid integers within the range 1–20.
- **Duplicate Guess Handling**: Penalizes players for guessing the same number multiple times by reducing their remaining chances.
- **Consecutive Guess Detection**: Tracks consecutive identical guesses and ends the game if the same number is guessed three times in a row.
- **Feedback**: Provides clear feedback for correct/incorrect guesses, duplicate guesses, and game outcomes.

## How to Play
1. Run the script in a Python environment.
2. Enter the number of chances you want to have to guess the number (must be a positive integer).
3. For each chance, input a number between 1 and 20.
4. The game provides feedback:
   - If the guess is correct, you win, and the game ends.
   - If the guess is incorrect, you get a hint to try again.
   - If you guess a number you've already guessed, you lose a chance but can try again in the same round.
   - If you guess the same number three times consecutively, the game ends.
5. The game ends when you guess the correct number, run out of chances, or guess the same number three times in a row.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/junayedhasansakib0/number-guessing-game.git
   ```
3. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```
4. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## Requirements
- Python 3.x
- No additional libraries are required beyond the standard `random` module.

## File Structure
- `number_guessing_game.py`: The main Python script containing the game logic.
- `README.md`: This file, providing an overview and instructions for the game.

## Example Gameplay
```
----Number Guessing Game----
How many times do you want to guess the number?: 5

--- Chance 1 of 5 ---
Enter a number between 1 and 20: 10
Incorrect!

--- Chance 2 of 5 ---
Enter a number between 1 and 20: 10
You have already guessed the number 10 before.
You lost one chance for guessing a duplicate. Remaining chances: 4

--- Chance 2 of 4 ---
Enter a number between 1 and 20: 15
Incorrect!

--- Chance 3 of 4 ---
Enter a number between 1 and 20: 12
Correct! You have guessed the number 12.
It took you 3 attempts.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate comments.

## Contact
For questions or suggestions, please open an issue on the GitHub repository or contact the maintainer at [junayedhasansakib009@gmail.com].