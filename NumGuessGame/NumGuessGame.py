import math
import random

def get_valid_number(prompt):
    """Prompt the user until a valid positive integer is entered."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # Check if input is a valid positive integer
            num = int(user_input)
            if num > 0:  # Check if greater than zero
                return num
            else:
                print("The number must be greater than zero. Please try again.")
        else:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Set your range (low_range and high_range)")

    # Get low_range with validation
    low_range = get_valid_number("Enter lower value of your range: ")

    # Get high_range with validation
    while True:
        high_range = get_valid_number("Enter higher value of your range: ")
        if high_range > low_range + 50:  # Ensure high_range is greater than low_range
            break
        else:
            print("The higher value must be at least more than 50 than lower value. Please try again.")

    print(f"Your range: {low_range} to {high_range}")

    total_numbers = high_range - low_range + 1
    min_guesses = math.ceil(math.log2(total_numbers))

    print(f"You have maximum guesses = {min_guesses}")

    guess = 0
    select_number = random.randint(low_range, high_range)

    while guess <= min_guesses:
        user_guess = get_valid_number("Enter your guess number : ")
        if user_guess == select_number:
            print(f"{50*'#'}\nCongrats! You have found the number")
            print(f"You have used {guess} of out {min_guesses} guesses")
            break
        else:
            guess += 1
            if user_guess < select_number:
                print("Your guess number is low. Try again")
            elif user_guess > select_number:
                print("Your guess number is High. Try again")
            elif guess == min_guesses:
                print("You are out of guesses. Game Lost!")


if __name__ == "__main__":
    main()
