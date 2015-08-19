from creature import Creature
from random import randint
import random


class Environment:
    """ Defines the boundary of a simulation and its properties """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.creatures = []
        self.color = (0, 0, 0)
        self.years = 0
        self.genepool = []

    def add_creature(self, x, y, color=None, size=None):
        """ Add a creature to the Environment"""
        creature = Creature(x, y, color, size)
        self.creatures.append(creature)

    def remove_creature(self):
        try:
            self.years += 1
            dead_creature = self.creatures.pop()
            for year in range(self.years):
                self.genepool.append(dead_creature)
        except IndexError:
            print "NEXT GENERATION!"
            creatures = random.sample(self.genepool, self.years)
            for creature in creatures:
                child = Creature(randint(0, 600), randint(0, 600), color=creature.color, size=creature.size)
                self.add_creature(child.x, child.y, child.color, creature.size)
            self.years = 0


