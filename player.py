import pygame

class Player:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0088.png')

        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (0, 0)

    def move_right(self):
        self.position = (self.position[0] + 64, self.position[1])

    def move_left(self):
        self.position = (self.position[0] - 64, self.position[1])

    def move_up(self):
        self.position = (self.position[0], self.position[1] - 64)

    def move_down(self):
        self.position = (self.position[0], self.position[1] + 64)