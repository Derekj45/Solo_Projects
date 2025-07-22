import random  # Import the random module to access its functions.

print("Welcome to the Word Scramble Game!")  # Intro message.
print("You will have 4 chances to guess the scrambled word!")

# List of possible words. This could also be imported from a separate file.
words = ["Buying", "Gullible", "Help", "Tractor", "Fight", "Tense", "Gaming", "Snake", "Driving", "Pneumonia"]

# Select a random word, convert it to a list of letters, and initialize scrambled_word.
word = random.choice(words)
letters = list(word)
scrambled_word = word

# Shuffle the letters until the scrambled word is different from the original.
while scrambled_word == word:
    random.shuffle(letters)
    scrambled_word = ''.join(letters)

print(scrambled_word)  # Display the scrambled word to the user.

# ch = total chances, gc = guess counter
ch = 4
gc = 0

# Game loop: user has up to 4 chances to guess the word.
while gc < ch:
    gc += 1
    guess = input("Enter your guess: ").strip()

    # Convert both guess and word to lowercase to ensure case-insensitive comparison.
    if guess.lower() == word.lower():
        print(f"Correct! The word is {word}. You guessed it in {gc} tries!")
        break

    elif guess.lower() != word.lower():
        print(f"Incorrect! Try again!")

    elif gc >= ch:
        print(f"Sorry! The word is {word}. Better luck next time!")
