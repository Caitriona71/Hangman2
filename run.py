# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

from words import word_list

print("Let's play hangman")

### Choose a random word
randomWord = random.choice(word_list)
