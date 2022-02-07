import random

class words:
    def __init__(self):
        self._word_list = ["roll", "terrasque", "dragon", "python", "create", "fall", "christmas", "parachute"]
        self.word = ""
        self.result=[] #list with hypens to replace by correct word
    
    def make_word(self):
        self.word = list(random.choice(self._word_list))
        for i in range(len(self.word)):
            self.result.append("_")
        return self.result
   