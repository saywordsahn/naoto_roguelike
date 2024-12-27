from settings import *
from game_object import GameObject


class Enemy(GameObject):

    def __init__(self, image_location):
        GameObject.__init__(self, image_location, Type.ENEMY)
        self.hp = 0
        self.ad = 0

    def take_damage(self, amount):
        self.hp -= amount

    def get_action(self, position, player_position):

        print(position)
        print(player_position)
        if abs(position[0] - player_position[0]) <= 1 or abs(position[1] - player_position[1]) <= 1:
            return EnemyBehavior.ATTACK

        return EnemyBehavior.MOVE

    def get_movement(self, position, world, player_position):

        if player_position[1] > position[1] and position[1] < NUM_COLS - 1:

            if world.get_adjacent_object(position, Direction.RIGHT) is None:
                return Direction.RIGHT

        elif player_position[1] < position[1] and position[1] > 0:

            if world.get_adjacent_object(position, Direction.LEFT) is None:
                return Direction.LEFT

        elif player_position[0] < position[0] and position[0] > 0:

            if world.get_adjacent_object(position, Direction.UP) is None:
                return Direction.UP

        elif player_position[0] > position[0] and position[0] < NUM_ROWS - 1:

            if world.get_adjacent_object(position, Direction.DOWN) is None:
                return Direction.DOWN


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
