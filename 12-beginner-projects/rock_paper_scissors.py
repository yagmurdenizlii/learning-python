import random

nb_rounds = 0

while (nb_rounds < 1):
    nb_rounds = int(input("Enter how many rounds you\'d like to play: "))


def letters_to_gestures(letter):
    map = {
        'R': "rock",
        'P': "paper",
        'S': "scissors",
    }
    return map.get(letter, "nothing")

def play(x): 

    computer_points = 0
    user_points = 0

    while(x > 0):
        user_plays = (input("Type R for rock, P for paper, S for scissors: ")).upper()
        print(f"You have played {letters_to_gestures(user_plays)}")

        computer_plays = random.choice(['R', 'P', 'S'])
        print(f"The computer has played {letters_to_gestures(computer_plays)}")

        if user_plays == 'R':
            if computer_plays == 'P':
                computer_points += 1
            if computer_plays == 'S':
                user_points += 1

        if user_plays == 'S':
            if computer_plays == 'R':
                computer_points += 1
            if computer_plays == 'P':
                user_points += 1

        if user_plays == 'P':
            if computer_plays == 'S':
                computer_points += 1
            if computer_plays == 'R':
                user_points += 1

        x += -1

        if(x == 1):
            plural = ''
        else:
            plural = 's'

        print(f"Computer: {str(computer_points)} User: {str(user_points)} \nYou have {str(x)} round{plural} left.")
    

    print(f"The game has ended.")

    diff = abs(computer_points - user_points)

    if(diff == 1):
        plural = ''
    else:
        plural = 's'

    
    if(computer_points > user_points):
        print(f"The winner is the computer by {str(diff)} points.")
    elif (computer_points < user_points):
        print(f"The winner is the user by {str(diff)} points.")
    else:
        print(f"There is a tie.")


play(nb_rounds)