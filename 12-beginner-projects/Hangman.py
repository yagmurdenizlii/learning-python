import random
import string

#first one is the filename, second one is the variable name
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words) 
    return word.upper()


def hangman():

    word = get_valid_word(words)

    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    word_letters = set(word)

    lives = 10

    while len(word_letters) > 0 and lives > 0:

        print('You have used these letters:', ' '.join(used_letters))
        print(f"You have {lives} lives left.")
        
        word_list = []
        #loops the word, puts - if that letter has already been used
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print('Current situation:', ' '.join(word_list)) #if we don't use join, there will be ' ' for every letter

        # Shorter way:
        # word_list = [letter if letter in used_letters else '-' for letter in word]
        # print("current word:", ' '.join(word_list))

        guessed_letter = input("Guess a letter: ").upper() 

        if guessed_letter in used_letters:
            print('You have already guessed this letter.')
        elif guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                print("This letter is in the word")
                word_letters.remove(guessed_letter)
            else:
                lives -= 1

    if lives == 0:
        print("You lost.")
    else:
        print(f"You have guessed the word {word} correctly.")


hangman()