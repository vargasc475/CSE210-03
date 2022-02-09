class gamestate:
    """A service that handles terminal operations.
    
    The responsibility of a gamestate is to store data for the game.
    """
     
    def __init__(self):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (gamestate): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        self.master_word = ""
        self.player_word = []
        self.guessed = []

    def set_word(self, new_word):
        self.master_word = new_word
        for _ in self.master_word:
            self.player_word.append("_")

    def determine_guess(self, guessed_letter):
        if guessed_letter in self.guessed:
            print("You already guessed this letter. Try another one.")
            found = True
            return found
        else:
            self.guessed.append(guessed_letter)
            z = -1
            found = False
            for _ in self.master_word:
                z += 1
                if guessed_letter == self.master_word[z]:
                    self.player_word[z] = str(guessed_letter)
                    found = True
            return found