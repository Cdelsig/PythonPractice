#Python3.7 - Automate The Boring Stuff - Al Sweigart

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
        if guess > secretNumber:
            print('Your guess is too high.')
        elif guess < secretNumber:
            print('Your guess is too low.')
        else:
            break #user guessed correctly
    except:
        print("You didn't enter a number!")

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')
