from enum import Enum

NUM_ROWS = 14
NUM_COLS = 22
CELL_SIZE = 64
PLAYER_START = (1, 1)
PLAYER_STARTING_HP = 10
WIDTH = CELL_SIZE * NUM_COLS
HEIGHT = CELL_SIZE * NUM_ROWS

class ItemType(Enum):
    ARMOR = 0,
    SWORD = 1,
    HEALTHPOT = 2

class Type(Enum):
    PLAYER = 0,
    ITEM = 1,
    ENEMY = 2

class Direction(Enum):
    LEFT = 0,
    RIGHT = 1,
    UP = 2,
    DOWN = 3