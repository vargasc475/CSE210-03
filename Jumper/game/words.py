import random

class Words:
    def __init__(self):
        self._word_list = ["peru", "venezuela", "chile", "crazil", "colombia", "ecuador", "argentina", "bolivia"]
        self.word = ""
        
    def make_word(self):
        self.word = list(random.choice(self._word_list))