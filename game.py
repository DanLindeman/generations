import pygame
from creature import Creature
from environment import Environment
import time
from random import randint
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Game(object):

    def __init__(self):
        pygame.display.set_caption('Generations')
        width, height = (600, 600)
        self.screen = pygame.display.set_mode((width, height))
        self.env = Environment(width, height)

    def add_creatures(self, number_of_creatures):
        for x in range(number_of_creatures):
            self.env.add_creature(x=randint(0,600), y=randint(0,600))

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
    game = Game()
    game.add_creatures(10)
    game.run_game()