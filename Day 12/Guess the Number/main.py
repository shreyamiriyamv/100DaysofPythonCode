from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
invalid_difficulty = True
no_of_guesses = 0
while invalid_difficulty:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        no_of_guesses = 10
        invalid_difficulty = False
    elif difficulty == "hard":
        no_of_guesses = 5
        invalid_difficulty = False
    else:
        print("Enter a valid difficulty!")

unguessed = True
while no_of_guesses != 0 and unguessed:
    print(f"You have {no_of_guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        unguessed = False
    elif guess > number:
        print("Too high.")
        no_of_guesses -= 1
    else:
        print("Too low.")
        no_of_guesses -= 1

    if no_of_guesses > 1:
        print("Guess again.")

if no_of_guesses == 0:
    print("You've run out of guesses. Refresh the page to run again!")