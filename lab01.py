import random

print("\nThis is the guess a number game.\nYou try to guess a random number in the smallest number of attempts.")

positive_int = int(input("Pick a positive integer: "))
guess_message = 0
random_int = random.randint(1, positive_int)
guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))
tally_guess = 0

while guess_message != random_int:
    tally_guess += 1
    list_guess = []
    if guess_message > random_int:
        print("   Too high!")
        guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))
    elif guess_message < random_int:
        print("   Too low!")
        guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))

list_guess.append(guess_message)

print(f"You were able to find the number in {tally_guess + 1} guesses.\nThe numbers you guessed were: {list_guess}")