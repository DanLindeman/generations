from creature import Creature
from random import randint
import random
import operator


class Environment:
    """ Defines the simulation pool, genepool, and its properties 
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.creatures = []
        self.color = (0, 0, 100)
        self.years = 0
        self.genepool = []

    def add_creature(self, x, y, color=None, size=None):
        """ Add a creature to the Environment
        """
        creature = Creature(x, y, color, size)
        self.creatures.append(creature)

    def remove_creature(self):
        """ Remove a creature from the genepool
        """
        try:
            self.years += 1
            dead_creature = self.creatures.pop()
            for year in range(self.years):
                self.genepool.append(dead_creature)
        except IndexError:
            creatures = random.sample(self.genepool, self.years)
            for creature in creatures:
                child = Creature(randint(0, 600), randint(0, 600), color=creature.color, size=creature.size)
                self.add_creature(child.x, child.y, child.color, creature.size)
            self.years = 0

    def enforce_selection_pressure(self):
        """Weight selection based on blue color
        """
        self.set_distance_from_pressure()
        self.creatures.sort(key=operator.attrgetter("distance_from_pressure"), reverse=False)
        self.remove_creature()

    def set_distance_from_pressure(self):
        for creature in self.creatures:
            creature.distance_from_pressure = abs(creature.color[2] - self.color[2])

