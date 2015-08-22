from random import randint

class Creature(object):
    """Class to represent a single Creature
    """

    def __init__(self, x, y, color=None, size=None):
        self.x = x
        self.y = y
        self.color = color
        if color == None:
            self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.size = size
        if size == None:
            self.size = randint(5, 20)
        self.thickness = 0 # indicates creature circles are filled in
        self.distance_from_pressure = None
