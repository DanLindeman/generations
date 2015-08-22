import pygame
from creature import Creature
from environment import Environment
import time
from random import randint
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Game(object):

    def __init__(self, max_population_size):
        pygame.display.set_caption('Generations')
        width, height = (800, 800)
        self.screen = pygame.display.set_mode((width, height))
        self.env = Environment(width, height, max_population_size)
        self.add_creatures()

    def add_creatures(self):
        for x in range(self.env.max_population_size):
            self.env.add_creature(x=randint(0,800), y=randint(0,800))

    def handle_event(self, event):
        running = True
        if event.type == pygame.QUIT:
            running = False
        return running

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                running = self.handle_event(event)
            self.screen.fill(self.env.color)
            self.env.enforce_selection_pressure()
            time.sleep(0.001)
            for creature in self.env.creatures:
                pygame.draw.circle(self.screen, creature.color, (int(creature.x), int(creature.y)), creature.size, creature.thickness)
            pygame.display.flip()

if __name__ == '__main__':
    game = Game(50)
    game.run_game()