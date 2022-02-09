from game.jumper import Jumper 
from game.words import Words
from game.GameState import GameState

class Director:

    def __init__(self):

        self._jumper = Jumper()
        self._words = Words()
        self._state = GameState()
        self._words.make_word()
        self._state.set_word(self._words.word)
        self.is_playing = True
        self.guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.do_outputs()
        while self.is_playing:
        
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        print("Good game!")

    def get_inputs(self):
        '''Get inputs from the user.
        
        Attribute (guess): letter from the user to guess the world.'''

        self.guess = input("\nPick a letter:\n")
       
    def do_updates(self):
        '''Update the panel with the guessed letter'''
        found = self._state.determine_guess(self.guess)
        if found:
            if not "_" in self._state.player_word:
                self.is_playing = False
        else:
            self.is_playing = self._jumper.take_damage()

    def do_outputs(self):
        self._jumper.make_panel(self._state.player_word)
        
        

