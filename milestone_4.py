import random

#Hangman class


class Hangman:
    # class attributes
    list_of_guesses = list()
    guess = str()
    word = str()
    word_guessed = []
    num_letters = int()
#
    def __init__(self, word_list, num_lives = 5):
        """
        Inintailises the class varibles bound to an instance of the class
        """
        self.word_list = word_list
        self.num_lives = num_lives

    #choseing word from inputted list
    def sel_word(self):
        """
        Selectes a word from the word list input, and sets up Hangman.word_guess list
        """
        Hangman.word = random.choice(self.word_list)
        Hangman.word_guessed = [str("_") for n in range(0,len(Hangman.word))]
        return Hangman.word

    # A function that checks weather the letter in the string parsed from ask_for_input() is in a string word.
    def check_guess(self, guess):
        """
        Checks weather the guess letter is in the word selected, manages num_letters and num lives.
        """
        Hangman.num_letters = len(Hangman.word)
        guess = guess.lower()
        if guess in Hangman.word:
                print(f'Good guess!')
                for n in range(0,len(Hangman.word)):
                    if guess == Hangman.word[n]:
                       Hangman.word_guessed[n] = guess
                       Hangman.num_letters = Hangman.num_letters -1
                print(Hangman.word_guessed)
                
                    
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives = self.num_lives -1
            print(f'You have {self.num_lives} lives left.')
        return
    
    # collect and validate input
    def ask_for_input(self):
        """
        Collects an input letter and chec its validity as a single letter of the alphabet.
        """
        col_inp_guess = True
        while col_inp_guess == True:
            guess = input('Enter a letter please, ')
            if len(guess) != 1 or guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif str(guess) in Hangman.list_of_guesses:
                print('You already tried that letter!')
                continue
            else:
                print(f'That works! {guess}')
                col_inp_guess = False
                Hangman.list_of_guesses.append(guess)
                Hangman(self).check_guess(guess)        
        return 





wordtran = Hangman(['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']).sel_word()      
Hangman.ask_for_input(wordtran)






