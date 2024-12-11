import pygame
import random as rand


class World:

    def __init__(self, num_rows, num_cols):
        self.rows = num_rows
        self.cols = num_cols
        self.CELL_SIZE = 64
        self.world = []
        self.rocks = pygame.image.load('dungeon/Tiles/tile_0049.png')
        self.rocks = pygame.transform.scale(self.rocks, (64, 64))
        self.dirt = pygame.image.load('dungeon/Tiles/tile_0048.png')
        self.dirt = pygame.transform.scale(self.dirt, (64, 64))
        self.generate_world()



    def generate_world(self):

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                r = rand.randint(0, 100)
                if r < 10:
                    row.append(self.rocks)
                else:
                    row.append(self.dirt)

            self.world.append(row)

    def draw_world(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                screen.blit(self.world[i][j], (j * self.CELL_SIZE, i * self.CELL_SIZE))