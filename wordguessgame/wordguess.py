import random  # Importing the random module to randomly select a word from the list

# Asking the player for their name and greeting them
name = input("What is your name? ")

print("Good Luck ! ", name)  # Displaying a welcome message to the player

# List of possible words for the guessing game
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Randomly choose a word from the list of words
word = random.choice(words)

print("Guess the characters")  # Prompting the player to start guessing

# Variable to keep track of guessed characters
guesses = ''

# Variable to store the number of remaining attempts
turns = 12

# Main game loop - continues as long as there are turns left
while turns > 0:

    failed = 0  # Counter for unguessed characters in the current word

    # Display the word progress (characters guessed or blanks for unguessed characters)
    for char in word:

        if char in guesses:  # If the character has been guessed, show it
            print(char, end=" ")

        else:  # Otherwise, display an underscore for the missing character
            print("_", end=" ")
            failed += 1  # Increment the failed counter for each missing character

    # If there are no unguessed characters left, the player wins
    if failed == 0:
        print("\nYou Win")  # Congratulate the player
        print("The word is: ", word)  # Reveal the word
        break  # Exit the game loop

    print()  # Move to the next line for better UI

    # Prompt the player to guess a character
    guess = input("guess a character:")

    # Add the guessed character to the `guesses` variable
    guesses += guess

    # Check if the guessed character is not in the word
    if guess not in word:

        # Reduce the remaining number of attempts
        turns -= 1
        print("Wrong")  # Inform the player about the incorrect guess
        print("You have", turns, 'more guesses')  # Show the remaining number of guesses

        # If no turns are left, the player loses the game
        if turns == 0:
            print("You Loose")  # Inform the player about losing the game
