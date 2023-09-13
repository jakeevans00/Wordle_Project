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

    def enter_action(s):
        print(s)
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Real word")
        else:
            gw.show_message("Not a real word")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    newWord = random.choice(FIVE_LETTER_WORDS)
    print(newWord)
    rows = N_ROWS
    cols = N_COLS
    for n in (range(0, len(newWord))):
        gw.set_square_letter(0, n, newWord[n])
# Startup code

if __name__ == "__main__":
    wordle()
