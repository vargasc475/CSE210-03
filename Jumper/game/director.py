from itertools import count
from game.jumper import Jumper 
from game.words import Words
from game.GameState import gamestate

class Director:

    def __init__(self):

        self._jumper = Jumper()
        self._words = Words()
        self._words.make_word()
        self._state = gamestate()
        self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # while self.is_playing:
        
        self.get_inputs()
        self.do_updates()
        self.do_outputs()

    def get_inputs(self):
        '''while waiting for Cannon, 
        Attribute (guess): letter to prove the panel.'''
        self.guess = "t"
       
    def do_updates(self):
        '''Update the panel with the guessed letter'''
        if self.guess in self._words.word:
            z = -1
            found = False
            for i in self._words.word:
                z += 1
                if self.guess == self._words.word[z]:
                    self._words.result[z] = self.guess
                    found = True
        else:
            pass   

    def do_outputs(self):
       self._jumper.make_panel(self._words.result)
       pass
        
        

