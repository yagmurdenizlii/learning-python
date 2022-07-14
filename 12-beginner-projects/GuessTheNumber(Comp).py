import random

def guess(x):
    nb = random.randint(1, x)
    guess = 0
    while (guess != nb):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if (guess < nb):
            print("Too low.")
        elif (guess > nb):
            print("Too high.")
    
    print("That is the corect number.")

