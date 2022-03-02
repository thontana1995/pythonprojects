import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry, guess again, Too low.')
        elif guess > randomNumber:
            print('Sorry, Guess again, Too high.')
    print(f'Congrats, You have guessed number {randomNumber} correctly!')

guess(10)

