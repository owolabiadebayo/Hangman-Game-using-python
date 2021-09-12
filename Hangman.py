# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
  # for windows
  if name == 'nt':
    _ = system('cls') 

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    

import hangman_words
# Display Hangman Logo
print(logo)
game_is_finished = False
lives = len(stages) - 1

# Choose random word from word_list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
print(f"Choosen word is: {chosen_word}")

# Create display for every letters are in the words chosen
display = []
for i in range(word_length):
  display += "_"

  print(display)

#Create a match letter for what is in play
while not game_is_finished:
    guess_letter = input('What is your guess word:').lower()

    clear()

    if guess_letter in display:
        print(f"You've already guessed{guess_letter}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter
        print(f"{' '.join(display)}")
    
    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not '_' in display:
        game_is_finished=True
        print("You win")    

    print(stages[lives])