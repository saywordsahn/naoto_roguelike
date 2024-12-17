import pygame
from game_object import GameObject

class Armor(GameObject):

    def __init__(self):
        GameObject.__init__(self, '../dungeon/Tiles/tile_0102.png')

class Sword:

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0103.png')

class HealthPot:

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0127.png')
