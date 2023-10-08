# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import importlib
import WordleGraphics

from WordleDictionary import ENGLISH_WORDS, ITALIAN_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    wordToGuess = random.choice(ENGLISH_WORDS)
    print(wordToGuess)
    WORDS = ENGLISH_WORDS
    language = "English"

    def enter_action(s):
        # Get color scheme
        scheme = gw.get_color_scheme()
        nonlocal WORDS
        nonlocal wordToGuess
        nonlocal language

        if scheme == "Original":
            CORRECT_COLOR = "#66BB66"
            PRESENT_COLOR = "#CCBB66"  # Brownish yellow for misplaced letters
            MISSING_COLOR = "#999999"

        elif scheme == "America":
            CORRECT_COLOR = "#0047AB"
            PRESENT_COLOR = "#D2042D"  # Brownish yellow for misplaced letters
            MISSING_COLOR = "#999999"

        # Get language from gw object
        lang = gw.get_language()
        print(wordToGuess)
        print(lang)
        print(language)
        print(len(WORDS))

        lettersUsed = []

        lettersLeft = list(wordToGuess)

        print(lettersLeft)

        # don't change word or dictionary if language is same
        if lang == language:
            print("in if")
            pass
        elif lang == "English":
            wordToGuess = random.choice(ENGLISH_WORDS)
            WORDS.clear()
            WORDS = ENGLISH_WORDS
            print(wordToGuess)
            language = lang
            lettersLeft.clear()
        elif lang == "Italian":
            WORDS.clear()
            print(len(WORDS))
            wordToGuess = random.choice(ITALIAN_WORDS)
            WORDS = ITALIAN_WORDS
            print(len(WORDS))
            language = lang
            lettersLeft.clear()
            print(wordToGuess)

        if s.lower() in WORDS:
            # Find all green colored squares
            print(len(wordToGuess))
            for n in range(0, len(wordToGuess)):
                letterGuess = gw.get_square_letter(gw.get_current_row(), n).lower()

                # if letter is in correct position, mark both square and key as green
                if letterGuess == wordToGuess[n]:
                    gw.set_square_color(gw.get_current_row(), n, CORRECT_COLOR)
                    gw.set_key_color(letterGuess.upper(), CORRECT_COLOR)
                    lettersLeft.remove(letterGuess.lower())
                    print(lettersLeft)
                else:
                    pass

            # Find all remaining letters (Yellow)
            for n in range(len(wordToGuess)):
                letterGuess = gw.get_square_letter(gw.get_current_row(), n).lower()

                # if square is colored correctly, keep going
                if gw.get_square_color(gw.get_current_row(), n) == CORRECT_COLOR:
                    pass
                # if letter is in the word, color yellow and remove from list of remaining letters
                elif letterGuess in lettersLeft:
                    print("in elif")
                    print(lettersLeft)
                    gw.set_square_color(gw.get_current_row(), n, PRESENT_COLOR)
                    if gw.get_key_color(letterGuess.upper()) == CORRECT_COLOR:
                        pass
                    else:
                        gw.set_key_color(letterGuess.upper(), PRESENT_COLOR)
                    lettersLeft.remove(letterGuess.lower())
                    print(lettersLeft)
                else:
                    gw.set_square_color(gw.get_current_row(), n, MISSING_COLOR)
                    if (
                        gw.get_key_color(letterGuess.upper()) == CORRECT_COLOR
                        or gw.get_key_color(letterGuess.upper()) == PRESENT_COLOR
                    ):
                        pass
                    else:
                        gw.set_key_color(letterGuess.upper(), MISSING_COLOR)

            if s.lower() == wordToGuess:
                gw.show_message(
                    "Congrats! Winner in " + str(gw.get_current_row() + 1) + "!!!"
                )
                return
            else:
                gw.set_current_row(gw.get_current_row() + 1)
                lettersUsed.clear()
        else:
            gw.show_message("Not a real word")

        return

    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
