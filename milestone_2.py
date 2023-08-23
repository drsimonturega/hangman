# Defining varibles for hangman game
import random

# Defining a fuction that selects a word from a list at random
def sel_word():
	# Defining a list of favorite fruits
	word_list = ['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']
	word = random.choice(word_list)
	print(f'{word}')
	return word

# Defining a function that takes a use input checks that is is a single chrater and alphabetical
def inp_guess():
	guess = input('Enter a letter please, ')
	if len(guess) == 1 and guess.isalpha() == True:
		print('Good guess!')
	else:
		print('Oops! That is not a valid input.')
	return guess

# Tempory code to check the above functions will need to think abaout making varibles global
sel_word()
sel_word()
#inp_guess()
print(f'{inp_guess()}')

