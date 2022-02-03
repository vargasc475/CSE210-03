import random

class words:
    def __init__(self):
        self._word_list = ["roll", "terrasque", "dragon", "python", "create", "fall", "christmas", "parachute"]
        self.word = ""
    
    def make_word(self):
        self.word = random.choice(self._word_list)