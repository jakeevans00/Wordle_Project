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
    # wordToGuess = random.choice(FIVE_LETTER_WORDS)
    wordToGuess = 'glass'
    tempList = wordToGuess
    print(wordToGuess)

    def enter_action(s):
        print(s)
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Real word")
            
            for n in range(0,len(wordToGuess)):

                if gw.get_square_letter(gw.get_current_row(),n).lower() == wordToGuess[n]:
                    gw.set_square_color(gw.get_current_row(),n,CORRECT_COLOR)
                elif gw.get_square_letter(gw.get_current_row(), n).lower() in tempList:
                    gw.set_square_color(gw.get_current_row(), n, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), n, MISSING_COLOR)
            
            if s.lower() == wordToGuess:
                gw.show_message("Congrats! Winner in " + str(gw.get_current_row()+1) + "!!!")
            else:
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not a real word")
        
        print(gw.get_current_row())
        return

    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

    # for n in (range(0, len(wordToGuess))):
    #     gw.set_square_letter(gw.get_current_row(), n, wordToGuess[n])
# Startup code

if __name__ == "__main__":
    wordle()
