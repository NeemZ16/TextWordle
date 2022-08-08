# Author: Neem Zaman
# Purpose: Text Wordle

import random
import csv

MAX_GUESSES = 5

with open('letters.csv', newline='') as f:
    reader = csv.reader(f)
    for words in reader:
        words

def main():
    print('There is a 5 letter secret word. You have {} guesses to get it.'.format(MAX_GUESSES))
    print('Clues:')
    print('G - Correct letter in correct place.')
    print('Y - Correct letter in incorrect place.')
    print('R - Incorrect letter')

    while True:  # Main game loop.
        secretWord = getSecretWord()

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = input('\nGuess #{}: '.format(numGuesses)).lower()
            # User validation loop:
            while len(guess) != 5 or guess.isdecimal():
                  guess = input('Invalid guess, try again: ')

            clues = getClues(guess, secretWord)
            print(clues)
            if numGuesses < MAX_GUESSES and guess != secretWord:
              print('You have {} guesses left.'.format(MAX_GUESSES - numGuesses))
            numGuesses += 1
            
            if guess == secretWord:
                break
            if numGuesses > MAX_GUESSES: 
                print('\nYou are out of guesses.')
                print('The answer was {}.\n'.format(secretWord))

        # Ask player if they want to play again.
        print('Enter yes to play again, anything else to exit: ')
        if not input('> ').lower() == 'yes':
            break
    print('Thanks for playing!')


def getSecretWord():
    nums = list(range(len(words)))

    random.shuffle(nums)

    secretWord = words[nums[13]].lower()
    return secretWord
  
def getClues(guess, secretWord):
    if guess == secretWord:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            # A correct letter in the correct place.
            clues.append('G')
        elif guess[i] in secretWord:
            # A correct letter in the incorrect place.
            clues.append('Y')
        elif guess[i] != secretWord[i]:
            # Not correct letter.
            clues.append('R')
    # Make a single string from the list of string clues.
    return ' '.join(clues)

# If the program is run (instead of imported), run the game (main fxn):
if __name__ == '__main__':
    main()