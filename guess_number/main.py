import random

print("Hello traveller! Welcome to my number guessing game!")
print("Please guess a number between 1 and 100.")

low = 1
high= 100

print("")
print(f"You have 7 chances to guess the number between {low} and {high}!")

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} tries!")
        break

    elif gc >= ch and guess != num:
        print(f"Sorry! The number is {num}. Better luck next time!")
    
    elif guess > num:
        print("Too high! Try again.")

    elif guess < num:
        print("Too low! Try again.")