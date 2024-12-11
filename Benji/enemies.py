import pygame

class Enemy:

    def __init__(self, image, x, y):
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)

class Bat(Enemy):

    def __init__(self, x, y):
        Enemy.__init__(self, pygame.image.load('../dungeon/Tiles/tile_0120.png'), x, y)

class Rat(Enemy):

    def __init__(self, x, y):
        Enemy.__init__(self, pygame.image.load('../dungeon/Tiles/tile_0123.png'), x, y)

class Spider(Enemy):

    def __init__(self, x, y):
        Enemy.__init__(self, pygame.image.load('../dungeon/Tiles/tile_0122.png'), x, y)