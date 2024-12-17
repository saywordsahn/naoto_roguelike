from enum import Enum

NUM_ROWS = 12
NUM_COLS = 12
CELL_SIZE = 64
PLAYER_START = (1, 1)

class Type(Enum):
    PLAYER = 0,
    ITEM = 1,
    ENEMY = 2

class Direction(Enum):
    LEFT = 0,
    RIGHT = 1,
    UP = 2,
    DOWN = 3