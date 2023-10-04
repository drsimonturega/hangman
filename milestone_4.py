import random

#Hangman class


class Hangman:
#
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        #self.word = word 
        self.word_guessed = []
        self.list_of_guesses = []
        self.word = None

    def sel_word(self):
    #     Defining a list of favorite fruits
        #word_list = ['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']
        self.word = random.choice(self.word_list)
        #print(f'{self.word}')
        return self.word



wordtran = Hangman(['apple', 'pear', 'blackcurrent', 'raspberry', 'mango']).sel_word()      
print(wordtran)
#WordTasks.sel_word()





