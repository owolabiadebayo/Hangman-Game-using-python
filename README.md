# Hangman Game using python
 Create a hangman game using python

_The word to guess is represented by a row of dashes, representing each letter of the word. In most variants, proper nouns, such as names, places, and brands, are not allowed. Slang words, sometimes referred to as informal or shortened words, are also not allowed. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions. If the suggested letter does not occur in the word, the other player draws one element of a hanged man stick figure as a tally mark.

The player guessing the word may, at any time, attempt to guess the whole word. If the word is correct, the game is over and the guesser wins. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. On the other hand, if the other player makes enough incorrect guesses to allow his opponent to complete the diagram, the game is also over, this time with the guesser losing. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed._


### python operation used

* python Looping
* Range
* random module
* Python Logical Operation

``` javascript 
0	
Hangman-0.  
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
Word:	hangman
Guess:	E
Misses:	
1	
Hangman-1.
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Word:	_ _ _ _ _ _ _
Guess:	T
Misses:	e
2	
Hangman-2.
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Word:	_ _ _ _ _ _ _
Guess:	A
Misses:	e, t
3	
Hangman-2.
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Word:	_ A _ _ _ A _
Guess:	O
Misses:	e, t
4	
Hangman-3.
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Word:	_ A _ _ _ A _
Guess:	I
Misses:	e, o, t
5	
Hangman-4.
  +---+
  |   |
  O   |
      |
      |
      |
=========
Word:	_ A _ _ _ A _
Guess:	S
Misses:	e, i, o, t
6	
Hangman-5.
  +---+
  |   |
      |
      |
      |
      |
=========
Word:	_ A _ _ _ A _
Guess:	N
Misses:	e, i, o, s, t
7	
Hangman-5
  +---+
      |
      |
      |
      |
      |
=========
Word:	_ A N _ _ A N
Guess:	R
Misses:	e ,i, o, s, t
8	
Hangman-6.
  +---+
      |
      |
      |
      |
      
=========
Word:	_ A N _ _ A N
Guess:	
Misses:	e, i, o, r, s, t
The guessing player has lost this game as the diagram had been completed before all the letters were guessed.
```