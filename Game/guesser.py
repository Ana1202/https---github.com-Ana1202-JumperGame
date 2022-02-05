#actor or Guesser in this case 
import random

class Guesser:
    """ the person trying to guess the word.
        This is where I set the global variables to be changed during game play"""
    def __init__(self):
        self.list = ["cat", "dog", "cow", "rat"]
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                        "v", "w", "x", "y", "z"]
        self.guesses = []
    def get_word(self):
       self.random_list = random.choice(self.list)
    def add_letter_to_dict(self, x):
       self.guesses.append(x)
