import pygame
import random as rand
from settings import *
from enemies import *
from player import *





class World:

    def __init__(self, player):
        self.tiles = []
        self.enemies = []
        self.player = player
        self.dirt = pygame.image.load('./dungeon/Tiles/tile_0048.png')
        self.dirt = pygame.transform.scale(self.dirt, (64, 64))

        self.rocks = pygame.image.load('./dungeon/Tiles/tile_0049.png')
        self.rocks = pygame.transform.scale(self.rocks, (64, 64))

        self.big_rocks = pygame.image.load('./dungeon/Tiles/tile_0042.png')
        self.big_rocks = pygame.transform.scale(self.big_rocks, (64, 64))

        self.wall = pygame.image.load('./dungeon/Tiles/tile_0037.png')
        self.wall = pygame.transform.scale(self.wall, (64, 64))

        self.generate_world()
        self.generate_enemies()

    def generate_enemies(self):

        for i in range(NUM_ROWS):
            row = []
            for j in range(NUM_COLS):
                r = rand.randint(0, 100)
                if r < 2:
                    row.append(Bat())
                else:
                    row.append(None)

            self.enemies.append(row)

    def generate_world(self):

        for i in range(NUM_ROWS):
            row = []
            for j in range(NUM_COLS):
                r = rand.randint(0, 100)
                if r < 10:
                    row.append(self.rocks)
                else:
                    row.append(self.dirt)

            self.tiles.append(row)

    def draw_tiles(self, screen):
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                screen.blit(self.tiles[i][j], (j * CELL_SIZE, i * CELL_SIZE))

    def draw_enemies(self, screen):
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if self.enemies[i][j] is not None:
                    screen.blit(self.enemies[i][j].image, (j * CELL_SIZE, i * CELL_SIZE))

    def draw_player(self, screen):
        position = (self.player.position[1] * 64, self.player.position[0] * 64)
        screen.blit(self.player.image, position)

    def draw_world(self, screen):
        self.draw_tiles(screen)
        self.draw_player(screen)
        self.draw_enemies(screen)

