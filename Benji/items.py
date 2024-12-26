from settings import *
from game_object import GameObject

class Armor(GameObject):

    def __init__(self):
        GameObject.__init__(self, '../dungeon/Tiles/tile_0102.png', Type.ITEM)
        self.item_type = ItemType.ARMOR

class Sword(GameObject):

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0103.png', Type.ITEM)
        self.item_type = ItemType.SWORD

class HealthPot:

    def __init__(self):
        GameObject.__init__(self, 'dungeon/Tiles/tile_0127.png', Type.ITEM)
        self.item_type = ItemType.HEALTHPOT
