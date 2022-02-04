from game.jumper import Jumper 

class Director:

    def __init__(self):

        self._jumper = Jumper()
        # self.is_playing = True

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
        pass
       
    def do_updates(self):
        pass

    def do_outputs(self):
        self._jumper.make_panel() 

