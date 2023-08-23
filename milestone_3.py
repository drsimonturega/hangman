
# milestone_3 code

# A function that takes a use input checks that is is a single chrater and alphabetical
def ask_for_input(): 
	col_inp_guess = True
	while col_inp_guess == True:
		guess = input('Enter a letter please, ')
		if len(guess) == 1 and guess.isalpha() == True:
			print('Good guess!')
			col_inp_guess = False
		else:
			print('Invalid letter. Please, enter a single alphabetical character.')
			continue
		return guess
word = 'apple'

# A function that checks weather the letter in the string parsed from ask_for_input() is in a string word.
def check_guess(guess):
	guess = guess.lower()
	if guess in word:
        	print(f'Good guess!')
	else:
        	print(f'Sorry, {guess} is not in the word. Try again.')
	return

check_guess(ask_for_input())

