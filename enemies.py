import pygame

class Bat:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0120.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)


class Rat:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0123.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)


class Spider:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0122.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)