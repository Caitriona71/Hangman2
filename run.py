# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

from words import word_list

print("Let's play hangman")

### Choose a random word
randomWord = random.choice(word_list)

for x in randomWord:
    print("_", end=" ")

def show_hangman(incorrect):
    if(incorrect == 0):
       print("\n+---+")
       print("     |")
       print("     |")
       print("     |")
       print("    ===")
    elif(incorrect == 1):
       print("\n+---+")
       print("O    |")
       print("     |")
       print("     |")
       print("    ===")                       
    elif(incorrect == 2):
       print("\n+---+")
       print("O    |")
       print("|    |")
       print("     |")
       print("    ===")                           
    elif(incorrect == 3):
       print("\n+---+")
       print(" O   |")
       print("/|   |")
       print("     |")
       print("    ===")
    elif(incorrect == 4):
       print("\n+---+")
       print(" O   |")
       print("/|\  |")
       print("     |")
       print("    ===")
    elif(incorrect == 5):
       print("\n+---+")
       print(" O   |")
       print("/|\  |")
       print("/    |")
       print("    ===")
    elif(incorrect == 6):
       print("\n+---+")
       print(" O   |")
       print("/|\  |")
       print("/ \  |")
       print("    ===")

def printWord(guessedLetters):
    counter=0
    correctLetters=0
    for char in randomWord:
      if(char in guessedLetters):
         print(randomWord[counter], end=" ")
         correctLetters+=1
      else:
         print(" ", end=" ")
      counter+=1
    return correctLetters

def printDashes():
   print("\r")
   for char in randomWord:
      print("\u203E", end=" ")

length_of_secret_word = len(randomWord)
attempts_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_correct = 0

while(attempts_wrong != 6 and current_letters_correct != length_of_secret_word):
   print("\nLetters guessed so far: ")
   for letter in current_letters_guessed:
      print(letter, end=" ")
   
   ### Prompt user for input
   letterGuessed = input("\nGuess a letter:")

   ### User is correct
   if(randomWord[current_guess_index]) == letterGuessed):


   
   
