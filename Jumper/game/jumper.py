from game.words import Words

class Jumper:

    def __init__(self):
        self.word = Words()
        self.word.make_word()

    def make_panel(self):
        for self._panel in self.word.result:
            print(self._panel, end=' ')
        
