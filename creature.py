from random import randint

class Creature(object):
    """Class to represent a single Creature
    """

    def __init__(self, x, y, color=None, size=None):
        self.x = x
        self.y = y
        self.color = color
        if not color:
            self.color = (0, 0, randint(0,255))
        self.size = size
        if not color:
            self.size = randint(5, 20)
        self.thickness = 0 # indicates creature circles are filled in
        self.distance_from_pressure = None

    def mutate_color(self):
        """Change one attribute randomly
        """
        self.color = (0, 0, randint(0,255))