# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# Was the syntax of Python the hardest part? If so, what part?
# Was there some aspect of the problem that was particularly difficult to solve?
# Was there an especially difficult bug? If so, how did you resolve it?
# Was there some difficulty with the instructions or any part of the problem definition?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import random

print("\nThis is the guess a number game.\nYou try to guess a random number in the smallest number of attempts.")

positive_int = int(input("Pick a positive integer: "))
guess_message = 0
random_int = random.randint(1, positive_int)
guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))
tally_guess = 0
list_guess = []

while guess_message != random_int:
    tally_guess += 1
    list_guess.append(guess_message)
    
    if guess_message > random_int:
        print("   Too high!")
        guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))

    elif guess_message < random_int:
        print("   Too low!")
        guess_message = int(input(f"Guess a number between 1 and {positive_int}: "))


list_guess.append(guess_message)
print(f"You were able to find the number in {tally_guess + 1} guesses.\nThe numbers you guessed were: {list_guess}")