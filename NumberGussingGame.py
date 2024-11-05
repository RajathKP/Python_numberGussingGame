#Problem: Number gussing game

import random

# generate random number between 1 and 100

number_to_guess= random.randint(1,100)

## Loop
while True:
        try:    # Ask the user to make a guess
                guess = int(input('Guess the number  between 1 and 100:'))
                # If the number < guess print too low
                if guess < number_to_guess:
                        print('Too low !')
                 # If the random number > guess print too high
                elif guess > number_to_guess:
                        print('Too High')
                else:
                        print('Congrats !! You Guess the number')

        # if it is not valid number, print error
        except ValueError:
                print('Please enter a valid number')












