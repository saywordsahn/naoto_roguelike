from settings import *
from game_object import GameObject


class Enemy(GameObject):

    def __init__(self, image_location):
        GameObject.__init__(self, image_location, Type.ENEMY)
        self.hp = 0

    def take_damage(self, amount):
        self.hp -= amount

    def get_movement(self, position, world, player_position):

        if player_position[1] > position[1] and position[1] < NUM_COLS - 1:

            if world.get_adjacent_object(position[0], position[1], Direction.RIGHT) is None:
                return Direction.RIGHT

        return None


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
