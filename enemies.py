import pygame

class Bat:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0120.png')
        self.image = pygame.transform.scale(self.image, (64, 64))


class Rat:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0123.png')
        self.image = pygame.transform.scale(self.image, (64, 64))



class Spider:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0122.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
