from settings import *
from game_object import GameObject

class Enemy(GameObject):

    def __init__(self, image_location):
        GameObject.__init__(self, image_location, Type.ENEMY)
        self.hp = 0

    def take_damage(self, amount):
        self.hp -= amount


class Bat(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0120.png')
        self.hp = 1

class Rat(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0123.png')
        self.hp = 1

class Spider(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0122.png')
        self.hp = 2