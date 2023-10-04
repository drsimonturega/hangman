import random

#Hangman class

class Hangman:
#
    def __init__(self, word_list, num_lives = 5):
        self.word_lisy = word_list
        self.num_lives = num_lives
        self.word = word 

    
class Words:

    def __init__(self, ):
        pass

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
        
class Characters:
    def __init___(self):
        pass

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


    # A function that checks weather the letter in the string parsed from ask_for_input() is in a string word.
    def check_guess(guess):
        guess = guess.lower()
        if guess in word:
            print(f'Good guess!')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
        return

