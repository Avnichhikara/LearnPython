# https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

import random  # Import the random module to randomly select a word

# List of possible words the game can choose from
word_list = ['python', 'developer', 'keyboard', 'laptop', 'function', 'variable']

# Randomly select a word from the list
word = random.choice(word_list)

# Create a set of unique letters in the word (to track which letters remain to be guessed)
word_letters = set(word)

# Keep track of letters the user has guessed
guessed_letters = set()

# Number of incorrect guesses allowed
attempts = 7

print("Welcome to the Word Guessing Game!")
print("You have", attempts, "attempts to guess the word.")

# Game loop: runs until the user either runs out of attempts or guesses all letters
while attempts > 0 and word_letters:
    # Display the current state of the word using a standard for loop
    display_word = []
    for letter in word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append('_')

    # Show the word with guessed letters revealed and unguessed letters as underscores
    print("Word: ", ' '.join(display_word))

    # Display letters guessed so far
    print("Guessed letters: ", ' '.join(sorted(guessed_letters)))

    # Ask the user for their guess and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # Validate input: must be a single alphabetic character
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue  # Skip to the next loop iteration

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guessed letter is in the word
    if guess in word_letters:
        # Remove the correctly guessed letter from the remaining letters
        word_letters.remove(guess)
        print("Good guess!")
    else:
        # Deduct an attempt for an incorrect guess
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

# Game over: check if the user guessed all letters
if not word_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
