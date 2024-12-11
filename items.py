import pygame

# armor 0102
# sword 0103
# health pot 0127

class Armor:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0102.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)


class Sword:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0103.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)


class HealthPot:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0127.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)