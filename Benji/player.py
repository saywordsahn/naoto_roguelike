import pygame
from game_object import GameObject
from settings import *


class Player(GameObject):

    def __init__(self):
        GameObject.__init__(self, '../dungeon/Tiles/tile_0088.png', Type.PLAYER)
        self.position = PLAYER_START
        self.hp = PLAYER_STARTING_HP
        self.armor_level = 0
        self.attack_damage = 1
        player_armor0 = pygame.image.load('../dungeon/Tiles/tile_0088.png')
        player_armor0 = pygame.transform.scale(player_armor0, (64, 64))

        player_armor1 = pygame.image.load('../dungeon/Tiles/tile_0085.png')
        player_armor1 = pygame.transform.scale(player_armor1, (64, 64))

        player_armor2 = pygame.image.load('../dungeon/Tiles/tile_0098.png')
        player_armor2 = pygame.transform.scale(player_armor2, (64, 64))

        player_armor3 = pygame.image.load('../dungeon/Tiles/tile_0097.png')
        player_armor3 = pygame.transform.scale(player_armor3, (64, 64))

        player_armor4 = pygame.image.load('../dungeon/Tiles/tile_0096.png')
        player_armor4 = pygame.transform.scale(player_armor4, (64, 64))
        self.images = [player_armor0, player_armor1, player_armor2, player_armor3,
                       player_armor4]

        self.image = self.images[self.armor_level]
        self.image = pygame.transform.scale(self.image, (64, 64))

    def upgrade_armor(self):
        self.armor_level += 1
        if self.armor_level < len(self.images):
            self.image = self.images[self.armor_level]

    def pick_up_item(self, item):

        if item.item_type == ItemType.ARMOR:
            self.upgrade_armor()

    def move(self, direction):

        if direction == Direction.RIGHT:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == Direction.LEFT:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == Direction.UP:
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == Direction.DOWN:
            self.position = (self.position[0] + 1, self.position[1])
