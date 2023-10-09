# Hangman
## Contents
* Introduction
* Milestone
* Varibles
* Functions
* Classes
* Running instructions

### Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Milestones
#### Milestone 1
Setting up the working environment, git hub and development folder.

#### Milestone 2

#### Milestone 3

#### Milestone 4
Putting functions in to the Hangman class and sorting out the attributes.

### Varibles
Key varibles used in the project.

#### word_list
A list of strings conating alphabetical text spelling out the name of five favouraite fruit.

#### word
A string containing a single entry from word list chosen at random.

#### guess
A single charater string, with an alphabetical value inputted by the user.

#### list_of_guesses
A list of letters guessed to highlight duplicate guesses.

#### word_guessed
A  list populated with a "_" for each letter in word. 

#### col_inp_guess
A boolean to control the input of guess.

### Functions
#### ask_for_input()
A function that takes a use input checks that is is a single chrater and alphabetical. 

#### check_guess(guess)
A function that checks weather the letter in the string parsed from ask_for_input() is in a string word. 

#### __init__
Initiates varibles bound to an instance of the class.

#### sel_word
Selectes a word from the word list input.

### Classes
#### Hangman
The class for the whole game.


### Running instructions
#### Currently
wordtran = Hangman(['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']).sel_word()      
Hangman.ask_for_input(wordtran)

