# Defining varibles for hangman game
import random
word_list = ['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']
#print(word_list[random.randrange(4)])
word = random.choice(word_list)
print(f'{word}')

guess = input('Enter a letter please, ')

if len(guess) == 1 and guess.isalpha() == True:
	print('Good guess!')
else:
	print('Oops! That is not a valid input.')



print(guess)

