# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    rows = N_ROWS
    cols = N_COLS
    guess = 0
    win = False
    wordToGuess = random.choice(FIVE_LETTER_WORDS)
    print(wordToGuess)

    def enter_action(s):
        print(s)
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Real word")
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not a real word")
        
        print(gw.get_current_row())
        return

    gw = WordleGWindow()
    print(gw.get_current_row())


    gw.add_enter_listener(enter_action)

    
    
    for n in (range(0, len(wordToGuess))):
        gw.set_square_letter(gw.get_current_row(), n, wordToGuess[n])
# Startup code

if __name__ == "__main__":
    wordle()
