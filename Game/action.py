#Action including words and graphics 

import random

words_list = ['russia', 'china', 'usa', 'canada', 'ghana'] #pre-made list of our words to guess

class Words:
    """this creates the random word and its responsability is 
        to keep track of attempts to take away parts of the chute
        atributes should be word to pick a word from the list
    """

    def _int_(self):
        self._word= random.choice(words_list)

        # Stores the hangman's body values
    hangman_values = ['___','/', '___','\\', '\\', '/', '\\', '/', 'o','/', '|', '\\', '/','\\',]
 
    # Stores the hangman's body values to be shown to the player
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ',' ', ' ',' ', ' ',]

    def print_chuteman(values):
        print()
        print("\t   {}".format(values[0]))
        print("\t {}{}{}".format(values[1], values[2], values[3]))
        print("\t {}  {} ".format(values[4], values[5]))
        print("\t {}  {}".format(values[6], values[7], ))
        print("\t   {}    ".format(values[8]))
        print("\t {}{}{}     ".format(values[9],values[10], values[11]))
        print("\t  {}{}       ".format(values[12], values[13]))
        print("               ")
        print("  `````````````````````")
        print()

