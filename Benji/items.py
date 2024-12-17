from settings import *
from game_object import GameObject

class Armor(GameObject):

    def __init__(self):
        GameObject.__init__(self, '../dungeon/Tiles/tile_0102.png', Type.ITEM)

class Sword:

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0103.png', Type.ITEM)

class HealthPot:

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0127.png', Type.ITEM)
