import pygame

class Armor:

    def __init__(self):
        self.image = pygame.image.load('../dungeon/Tiles/tile_0102.png')
        self.image = pygame.transform.scale(self.image, (64, 64))