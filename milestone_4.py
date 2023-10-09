import random

#Hangman class


class Hangman:
    list_of_guesses = list()
    guess = str()
    word = str()
    word_guessed = []
#
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = []
        #self.word = str()
        #self.guess = str()
        #self.list_of_guesses = list()
        

    def sel_word(self):
        #Defining a list of favorite fruits
        Hangman.word = random.choice(self.word_list)
        Hangman.word_guessed = [str("_") for n in range(0,len(Hangman.word))]
        print(f'{Hangman.word}, {Hangman.word_guessed}')
        return Hangman.word

    # A function that checks weather the letter in the string parsed from ask_for_input() is in a string word.
    def check_guess(self, guess):
        print(guess)
        guess = guess.lower()
        print(Hangman.word)
        if guess in Hangman.word:
                print(f'Good guess!')
                print(f'{Hangman.list_of_guesses}, {Hangman.word}, {Hangman.word_guessed}')
        else:
            print(f'Sorry, {guess} is not in the word, {self.word}. Try again.')
            print(f'{Hangman.list_of_guesses}, {Hangman.word}, {Hangman.word_guessed}')
        return

    def ask_for_input(self):
        #list_of_guesses = list()
        #print(f' {self.word}, {self.guess}')
        col_inp_guess = True
        while col_inp_guess == True:
            guess = input('Enter a letter please, ')
            #self.guess = str(guess)
            if len(guess) != 1 or guess.isalpha() != True:
                print(guess)
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif str(guess) in Hangman.list_of_guesses:
                print('You already tried that letter!')
                continue
            else:
                print(f'That works! {guess}')
                col_inp_guess = False
                #self.guess = guess
                #Hangman.list_of_guesses = Hangman.list_of_guesses.append('guess')
                Hangman.list_of_guesses.append(guess)
                Hangman(self).check_guess(guess)
                #Hangman.list_of_guesses.append('guess')
            
            
        return #guess
#word = 'apple'




wordtran = Hangman(['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']).sel_word()      
Hangman.ask_for_input(wordtran)






