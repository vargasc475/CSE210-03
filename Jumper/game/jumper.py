from game.words import Words

class Jumper:

    def __init__(self):
        self.word = Words()
        self.word.make_word()

    def make_panel(self, word):
        '''Make the panel'''
        for self._panel in word:
            print(self._panel, end=' ')            

        
