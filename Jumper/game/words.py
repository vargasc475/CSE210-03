import random

class Words:
    def __init__(self):
        self._word_list = ["peru", "venezuela", "chile", "brazil", "colombia", "ecuador", "argentina", "bolivia", "uruguay", "panama", "nicaraguq", "honduras", "cuba", "guatemala", "columbia", "mexico"]
        self.word = ""
        
    def make_word(self):
        self.word = list(random.choice(self._word_list))