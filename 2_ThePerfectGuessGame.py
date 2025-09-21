''''
We r going to wap that generates the random no. and asks the user to guess it.

If the player guess is higher than the actual no. , then the program displays 
"Lower number please ". Similarly, if the user's guess is too low, the program
prints "higher number please". When the user guesses the correct no. , the 
program displays number of guesses the player uses to arrive at the number.
'''

import random

correct_guess = random.randint(1,100)

print("===The Perfect Guess===")

guess = None
attempts = 0

while guess !=  correct_guess:
    guess = int(input("Enter your guess nah brooo : "))
    attempts+=1

    if guess < correct_guess:
        print("Too low, Try again!!")

    elif guess > correct_guess:
        print("Too high, Try again!!")

    else:
        print(f"Corect Guess wohooo 🥳 . You guessed it in {attempts} attempts")
