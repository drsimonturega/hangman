import random

#Hangman class
class Hangman():
    
    
    def __init__(self, word_list, num_lives):
        """Inintailises the class varibles bound to an instance of the class"""
        list_of_guesses = list()
        self.list_of_guesses = list_of_guesses
        guess = str()
        word = str()
        self.word = word
        word_guessed = []
        self.word_guessed = word_guessed
        list_of_guesses = []
        self.list_of_guesses = list_of_guesses
        num_letters = int()
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list

    #choseing word from inputted list
    def sel_word(self):
        """
        Selectes a word from the word list input, and sets up 
        self.word_guess list

        Keyword arguments:
        word -- A string containing a single entry from word list chosen at random.
        word_guessed -- A list populated with a "_" for each letter in word.
        num_letters -- The number of letters left to guess from word.
        """
        self.word = random.choice(self.word_list)
        self.word_guessed = [str("_") for n in range(0,len(self.word))]
        self.num_letters = len(self.word)
        return self.word, self.word_guessed, self.num_letters

    # A function that checks weather the letter in the string parsed 
    # from ask_for_input() is in a string word.
    def check_guess(self, guess):
        """
        Checks weather the guess letter is in the word selected, 
        manages num_letters and num lives.

        Keyword arguments:
        num_letters -- The number of letters left to guess from word.
        word -- A string containing a single entry from word list chosen at random.
        word_guessed -- A list populated with a "_" for each letter in word.
        """
        guess = guess.lower()
        if guess in self.word:
                print(f'Good guess!')
                for n in range(0,len(self.word)):
                    if guess == self.word[n]:
                       self.word_guessed[n] = guess
                       self.num_letters = self.num_letters -1
                print(self.word_guessed)                 
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives = self.num_lives -1
            print(f'You have {self.num_lives} lives left.')
            #num_lives = self.num_lives
        return #num_lives
    
    # collect and validate input
    def ask_for_input(self):
        """
        Collects an input letter and checks its validity as a single 
        letter of the alphabet.

        Keyword arguments:
        list_of_guesses -- A list of letters guessed to highlight duplicate guesses.
        col_inp_guess -- A boolean to control the input of guess.

        Varibles:
        guess -- A single charater string, with an alphabetical value inputted by the user.
        """
        col_inp_guess = True
        while col_inp_guess == True:
            guess = input('Enter a letter please, ')
            if len(guess) != 1 or guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif str(guess) in self.list_of_guesses:
                print('You already tried that letter!')
                continue
            else:
                #col_inp_guess = False
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break       
        return 


def play_game(word_list):
    """
    Runs hangman class and controls the functions with in using  a 
    while loop. It takes a list of fruit or other words as an argument.

    Keyword arguments:
    num_letters -- The number of letters left to guess from word.
    num_lives -- Number of lives, thats incorrect guesses left starting at five as a default.
    game_loop_contr -- Boolean that controls the while loop in the play_game() function. Containns the win and loose conditions.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.sel_word()
    print(f'You have {num_lives} lives')
    game_loop_contr = True
    while game_loop_contr == True:
        if game.num_lives == 0:
             print("You lost")
             game_loop_contr = False
        elif  game.num_letters > 0:
            Hangman.ask_for_input(game)
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            game_loop_contr = False

play_game(['apple', 'pear', 'blackcurrent', 'raspberry', 'mango'])