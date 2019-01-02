#Hangman
#Sabastian Taton
#Nov. 26 2018

import time
import random

global MAX_WRONG
global WORDS
global word
global so_far
global wrong
global used

HANGMAN = (
"""
-------
|     |
|     |
|
|
|
|
|
--------
"""
,
"""
-------
|     |
|     |
|     0
|
|
|
|
---------
"""
,
"""
-------
|     |
|     |
|     O
|     +
|
|
|
---------
"""
,
"""
-------
|     |
|     |
|     O
|    /+
|
|
|
----------
"""
,
"""
-------
|     |
|     |
|     O
|    /+/
|
|
|
----------
"""
,
"""
-------
|     |
|     |
|     O
|    /+/
|    |
|
|
----------
"""
,
"""
-------
|     |
|     |
|     O
|    /+/
|    ||
|
|
----------
""")

WORDS = ("CODE","COMMENT","STRING","FLOAT","LIST","APPEND","INSERT","FUNCTION","IMPORT","PASS")
MAX_WRONG = len(HANGMAN)


def main():
    print("Welcome to Hangman. Have Fun!")
    input("Press enter to play!")
    play()
    
def play():
    word = random.choice(WORDS)#word to guess
    so_far = "-" * len(word)#one dash for each letter in guess word
    wrong = 0 #number of wrong guesses
    used = []#letters already guessed
    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("You have used the following letters:\n",used)
        print("\nSo far, the word is:\n",so_far)

        guess = input("\n\nEnter your guess:")
        guess = guess.upper()

        while guess in used:
            print("You have already used the letter",guess)
            guess = input("\n\nEnter your guess:")
            guess = guess.upper()
        used.append(guess)

        if guess in word:
            print("\n",guess,"is in the word!")
            new = ""
            
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print("\n",guess,"is not in the word")
            wrong += 1

    if so_far == word:
        win()

    if wrong == MAX_WRONG:
        wrong-=1
        print(HANGMAN[wrong])
        print("\nYou've been hanged")

def win():
    print("\nYou guessed it!")

    print("\nThe word is",word)

    input("Press enter to exit")

main()











































































        
