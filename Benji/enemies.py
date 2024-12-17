from settings import *
from game_object import GameObject

class Enemy(GameObject):

    def __init__(self, image_location):
        GameObject.__init__(self, image_location, Type.ENEMY)


class Bat(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0120.png')

class Rat(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0123.png')

class Spider(Enemy):

    def __init__(self):
        Enemy.__init__(self, '../dungeon/Tiles/tile_0122.png')