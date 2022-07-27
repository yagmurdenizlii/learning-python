import random

x = -1
y = -1

while(x < 0):
    x = int(input("Give a min integer: "))
while(y <= x):
    y = int(input(f"Give a max integer, greater than {str(x)}: "))

def guess(x, y):

    comparison = ''

    while(comparison != 0):
        if(x != y):
            guess = random.randint(x, y)
        else:
            guess = x

        comparison = int(input(f'Is your number {str(guess)}? (Type a negative integer if your number is smaller, a positive number if your number is bigger, 0 if it is equal)'))

        if(comparison < 0):
            y = guess - 1
        elif(comparison > 0):
            x = guess + 1

    print("I have guessed correctly!!")


guess(x, y)



    
    

