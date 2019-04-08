from core.color import Color

class Puyo:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return str(self.color)
    
    def __eq__ (self, otherPuyo):
        return isinstance(otherPuyo, Puyo) and \
               self.color == otherPuyo.color

