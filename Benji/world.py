import pygame
import random as rand
from items import *
from settings import *

class World:

    def __init__(self):
        self.rows = 12
        self.cols = 12
        self.world = []
        self.empty_tiles = []
        self.item_map = [[None for i in range(self.cols)] for j in range(self.rows)]

        self.dirt = pygame.image.load('../dungeon/Tiles/tile_0048.png')
        self.dirt = pygame.transform.scale(self.dirt, (64, 64))

        self.rocks = pygame.image.load('../dungeon/Tiles/tile_0049.png')
        self.rocks = pygame.transform.scale(self.rocks, (64, 64))

        self.big_rocks = pygame.image.load('../dungeon/Tiles/tile_0042.png')
        self.big_rocks = pygame.transform.scale(self.big_rocks, (64, 64))

        self.wall = pygame.image.load('../dungeon/Tiles/tile_0037.png')
        self.wall = pygame.transform.scale(self.wall, (64, 64))



    def can_pass(self):
        return True

    def item_exists(self, row, col):
        return self.item_map[row][col] is not None

    def get_item(self, row, col):
        return self.item_map[row][col]

    def get_coords(self, x, y):
        return x * CELL_SIZE, y * CELL_SIZE

    def generate_items(self):

        for i in range(rand.randint(3, 5)):
            random_cell = rand.choice(self.empty_tiles)
            self.empty_tiles.remove(random_cell)
            armor = Armor()
            self.item_map[random_cell[0]][random_cell[1]] = armor


    def generate_world(self):

        for i in range(self.rows):
            row = []
            for j in range(self.cols):

                # for border generation
                # if i == 0 or j == 0 or i == self.rows - 1 or j == self.rows - 1:
                #     row.append(self.wall)
                # else:
                r = rand.randint(0, 100)
                if r < 10:
                    row.append(self.rocks)
                elif r < 12:
                    row.append(self.big_rocks)
                else:
                    row.append(self.dirt)

                self.empty_tiles.append((i, j))
            self.world.append(row)

        self.generate_items()

    def draw_world(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                screen.blit(self.world[i][j], (j * CELL_SIZE, i * CELL_SIZE))

                if self.item_map[i][j] is not None:
                    screen.blit(self.item_map[i][j].image, (j * CELL_SIZE, i * CELL_SIZE))
