import pygame


class Bat:

    def __init__(self):
        self.hp = 1
        self.ad = 1
        self.image = pygame.image.load('dungeon/Tiles/tile_0120.png')
        self.image = pygame.transform.scale(self.image, (64, 64))


class Rat:

    def __init__(self):
        self.hp = 2
        self.ad = 1
        self.image = pygame.image.load('dungeon/Tiles/tile_0123.png')
        self.image = pygame.transform.scale(self.image, (64, 64))


class Spider:

    def __init__(self):
        self.hp = 3
        self.ad = 2
        self.image = pygame.image.load('dungeon/Tiles/tile_0122.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
