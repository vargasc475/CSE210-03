from itertools import count
from game.jumper import Jumper 
from game.words import words

class Director:

    def __init__(self):

        self._jumper = Jumper()
        self._words = Words()
        self._words.make_word()
        # self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
        
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        '''while waiting for Cannon, 
        Attribute (guess): letter to prove the panel.'''
        self.input_letters=[]
        
        self.input_letter=input("Enter a letter [a-z]:")
        if self.input_letter in self.input_letters:
            print("You already said that letter")
        elif  self.input_letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter a letter [a-z]: ")
        else:
            self.input_letter.append(self.input_letter)
            
       
    def do_updates(self):
        '''Update the panel with the guessed letter'''
        z = -1
        found = False
        for i in self._words.word:
            z += 1
            if self.guess == self._words.word[z]:
                self._words.result[z] = self.guess
                found = True
           
        for i in range(len(self.word)):
            if  self.word[i]==self.input_letter:
                self.result[i]=self.input_letter
        if self._words.result==self._words.word:
            print("You win!")
    def do_outputs(self):
        self._jumper.make_panel(self._words.result) 
        
        