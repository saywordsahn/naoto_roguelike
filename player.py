import pygame
from settings import *

class Player:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0088.png')
        self.hp = 10
        self.ad = 1
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = PLAYER_START

    def move_right(self):
        self.position = (self.position[0], self.position[1] + 1)

    def move_left(self):
        self.position = (self.position[0], self.position[1] - 1)

    def move_up(self):
        self.position = (self.position[0] - 1, self.position[1])

    def move_down(self):
        self.position = (self.position[0] + 1, self.position[1])