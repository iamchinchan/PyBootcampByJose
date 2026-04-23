"""
Game for guessing the number
"""
import random
import sys
import os
CHANCES = 10


def check_out_of_bounds(num: int) -> bool:
    """Checks value out of bounds or not"""
    return (num < 1 or num > 100)


def input_a_number() -> int:
    """Asking user for a int input"""
    while True:
        try:
            return int(input("Guess a number between 1 and 100:\n"))
        except ValueError:
            print("Please enter a Whole number between 1 and 100, Try Again: ")


def screen_logger(text: str, number_of_guesses_left: int) -> None:
    """Telling player about his guesses left"""
    print(f"{text}: You have {number_of_guesses_left} chances left")


def main():
    """game Logic"""
    hidden_number = random.randint(1, 100)
    number_of_guesses_left = CHANCES
    guess_value = None
    last_guess_value = None
    print("Welcome to Guessing Game! You have ten chances left")
    print(f"printing hidden number just for testing: {hidden_number}")
    while guess_value != hidden_number and number_of_guesses_left > 0:
        guess_value = input_a_number()
        number_of_guesses_left -= 1
        if guess_value == hidden_number:
            print(
                f"Guessed correctly in {hidden_number} in {CHANCES-number_of_guesses_left} guesses")
            break
        if check_out_of_bounds(guess_value):
            screen_logger("Out of Bounds!", number_of_guesses_left)
            continue
        how_close_now = abs(hidden_number-guess_value)
        if last_guess_value is None:
            if how_close_now <= 10:
                text = "Warm!"
            else:
                text = "Cold!"
        else:
            how_close_last_time = abs(hidden_number-last_guess_value)
            if how_close_last_time == how_close_now:
                text = "Same Margin!"
            elif how_close_now < how_close_last_time:
                text = "Warmer!"
            else:
                text = "Colder!"
        screen_logger(text, number_of_guesses_left)
        last_guess_value = guess_value

    else:
        if number_of_guesses_left == 0:
            print(
                f"You've run out of {CHANCES} chances, correct number was {hidden_number}")


if __name__ == "__main__":

    # 1. Show the path to the actual Python 'brain' being used
    print(f"Python Executable: {sys.executable}")

    # 2. Show the Python version
    print(f"Python Version:    {sys.version}")

    # 3. Show the name of the active Conda environment (if applicable)
    print(f"Conda Env:         {os.environ.get('CONDA_DEFAULT_ENV')}")

    main()
