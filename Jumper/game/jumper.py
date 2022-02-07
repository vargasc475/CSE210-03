from game.words import Words

class Jumper:

    def __init__(self):
        self.word = Words()
        self.word.make_word()
        self.word.get_letter()

    def make_panel(self, word):
        '''Make the panel'''
        for self._panel in word:
            print(self._panel, end=' ')
    
    def make_jumper(self):
        self.failures=0
        self.parachute =["    ___  ",
                         "   /___\ ",
                         "   \   / ",
                         "    \ /  ",   
                         "     O ", 
                         "    /|\ ",   
                         "    / \ ",
                         "^^^^^^^^^^^^"]

        for i in range (len(self.parachute)-self.failures):
            print(self.parachute[i+self.failures])
        
    
        if self.input_letter not in self.word.word:
            self.failures+=1
           
        if self.failures>4:
            print("The word was:", "".join(self.word.word))
            print("Game over")

