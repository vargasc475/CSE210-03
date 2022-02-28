from game.words import Words

class Jumper:

    def __init__(self):
        self.word = Words()
        self.word.make_word()
        self.health = [
            "\n  ___ ",
            "\n /■■■\ ",
            "\n/■■■■■\ ",
            "\n\■■■■■/",
            "\n \■■■/",
            "\n   ☺",
            "\n  /|\ ",
            "\n  / \ \n",
            "  ^^^^^^^"
            ]

    def make_panel(self, word):
        '''Make the panel'''
        jumpster = ""
        for panel in word:
            jumpster += f"{panel} "
        for i in self.health:
            jumpster += i
        print(jumpster)
    
    def take_damage(self):
        '''Reduce health, and return a game over Bool'''
        self.health.pop(0)
        out = len(self.health) > 4
        return out
        
