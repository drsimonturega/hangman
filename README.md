# Hangman
## Contents
* Introduction
* Milestone
* Functions
* Classes
* Running instructions

### Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Milestones
#### Milestone 1
Setting up the working environment, git hub and development folder. The git hub is set up and will be used through out the project.

#### Milestone 2
Here we create the key varibles for the game, building the sel_word() and inp_guess() functions. This involves creating a list of words, choosing one word then begining the process of collecting user input and checking that inout is a single charater. The initial code is refactored and optimized then code was updated on GitHub. Below is an example of the inital inp_guess function, this was achived by using the len() and isalpha() functions.

```
def inp_guess():
    guess = input('Enter a letter please, ')
    if len(guess) == 1 and guess.isalpha() == True:
        print('Good guess!')
    else:
        print('Oops! That is not a valid input.')
    return guess
```

#### Milestone 3
Check if the guessed charcter is in the word building the check_guess() and ask_for_input() functions. The check_guess function uses an ```if``` statment to search for the letter from th the user input is in the chosen word. 

 ![Alt](/mil_3.png "milestone_3")

The code was then refactored and optimized uppdating on the remote repository with a push command. The documentation was updated on the GitHub remote repository and synced with the local repository using a pull command.

#### Milestone 4
Putting functions in to the Hangman class and sorting out the attributes. The Hangman class was built with an __init__ function to initiate the class varibles bound to an instance of the class. Functions from prevous milestones were added to this class.

![Alt](/code_ms_4.png "milestone_4")


#### Milestone 5
Putting all together with the play_game() function.

### Functions
#### ask_for_input()
A function that takes a use input checks that is is a single chrater and alphabetical. 

Keyword arguments:
list_of_guesses -- A list of letters guessed to highlight duplicate guesses.
col_inp_guess -- A boolean to control the input of guess.

Varibles:
guess -- A single charater string, with an alphabetical value inputted by the user.

#### check_guess(guess)
A function that checks weather the letter in the string parsed from ask_for_input() is in a string word. 

Keyword arguments:
num_letters -- The number of letters left to guess from word.
word -- A string containing a single entry from word list chosen at random.
word_guessed -- A list populated with a "_" for each letter in word.

Varibles:
guess -- A single charater string, with an alphabetical value inputted by the user.

#### __init__
Initiates varibles bound to an instance of the class.

#### sel_word
Selectes a word from the word list input.

Keyword arguments:
word -- A string containing a single entry from word list chosen at random.
word_guessed -- A list populated with a "_" for each letter in word.
num_letters -- The number of letters left to guess from word.

#### play_game
Function that initiates Hangman class and controls the while loop that calculates weather you are playing, have lost or have won.

Keyword arguments:
num_letters -- The number of letters left to guess from word.
num_lives -- Number of lives, thats incorrect guesses left starting at five as a default.
game_loop_contr -- Boolean that controls the while loop in the play_game() function. Containns the win and loose conditions.


### Classes
#### Hangman
The class for the whole game.


### Running instructions
#### Final
python3 ./milestone_5.py

### License information
This is availible through a [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.html "GNU General Public License, version 3").
