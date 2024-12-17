from enum import Enum

NUM_ROWS = 12
NUM_COLS = 12
CELL_SIZE = 64

class Type(Enum):
    PLAYER = 0,
    ITEM = 1,
    ENEMY = 2