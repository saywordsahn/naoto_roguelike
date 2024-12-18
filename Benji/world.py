import pygame
import random as rand
from items import *
from enemies import *
from settings import *


class CellData:

    def __init__(self, tile, pos):
        self.position = pos
        self.tile = tile
        self.object = None

class World:

    def __init__(self):
        self.rows = 12
        self.cols = 12
        self.world = []
        self.empty_tiles = []

        # self.item_map = [[None for i in range(self.cols)] for j in range(self.rows)]

        self.dirt = pygame.image.load('../dungeon/Tiles/tile_0048.png')
        self.dirt = pygame.transform.scale(self.dirt, (64, 64))

        self.rocks = pygame.image.load('../dungeon/Tiles/tile_0049.png')
        self.rocks = pygame.transform.scale(self.rocks, (64, 64))

        self.big_rocks = pygame.image.load('../dungeon/Tiles/tile_0042.png')
        self.big_rocks = pygame.transform.scale(self.big_rocks, (64, 64))

        self.wall = pygame.image.load('../dungeon/Tiles/tile_0037.png')
        self.wall = pygame.transform.scale(self.wall, (64, 64))

    def get_adjacent_cell(self, position, direction):
        if direction == Direction.RIGHT:
            return self.world[position[0]][position[1] + 1]
        elif direction == Direction.LEFT:
            return self.world[position[0]][position[1] - 1]
        elif direction == Direction.UP:
            return self.world[position[0] - 1][position[1]]
        elif direction == Direction.DOWN:
            return self.world[position[0] + 1][position[1]]

    def get_cells_with_enemies(self):

        cells_with_enemies = []

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                cell = self.world[i][j]
                if cell.object is not None and cell.object.type == Type.ENEMY:
                    cells_with_enemies.append(cell)

        return cells_with_enemies

    def get_adjacent_object(self, position, direction):
        return self.get_adjacent_cell(position, direction).object

    def move_object(self, position, direction):
        if direction == Direction.RIGHT:
            self.world[position[0]][position[1] + 1].object = self.world[position[0]][position[1]].object
            self.world[position[0]][position[1]].object = None
        elif direction == Direction.LEFT:
            self.world[position[0]][position[1] - 1].object = self.world[position[0]][position[1]].object
            self.world[position[0]][position[1]].object = None
        elif direction == Direction.UP:
            self.world[position[0] - 1][position[1]].object = self.world[position[0]][position[1]].object
            self.world[position[0]][position[1]].object = None
        elif direction == Direction.DOWN:
            self.world[position[0] + 1][position[1]].object = self.world[position[0]][position[1]].object
            self.world[position[0]][position[1]].object = None

    def add_object_to_cell(self, object, row, col):
        self.world[row][col].object = object

    def remove_game_object(self, position):
        self.world[position[0]][position[1]].object = None

    def remove_game_object(self, position, direction):
        cell = self.get_adjacent_cell(position[0], position[1], direction)
        cell.obj = None

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
            self.add_object_to_cell(armor, random_cell[0], random_cell[1])

    def generate_enemies(self):

        for i in range(rand.randint(3, 5)):
            random_cell = rand.choice(self.empty_tiles)
            self.empty_tiles.remove(random_cell)
            enemy = Spider()
            self.add_object_to_cell(enemy, random_cell[0], random_cell[1])

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
                    row.append(CellData(self.rocks, (i, j)))
                elif r < 12:
                    row.append(CellData(self.big_rocks, (i, j)))
                else:
                    row.append(CellData(self.dirt, (i, j)))

                self.empty_tiles.append((i, j))
            self.world.append(row)

        # remove starting point for player
        self.empty_tiles.remove(PLAYER_START)
        self.generate_items()


    def draw_world(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                screen.blit(self.world[i][j].tile, (j * CELL_SIZE, i * CELL_SIZE))

                if self.world[i][j].object is not None:
                    screen.blit(self.world[i][j].object.image, (j * CELL_SIZE, i * CELL_SIZE))
