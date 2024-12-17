import pygame
import settings
from Benji.settings import CELL_SIZE


class GameObject:

    def __init__(self, file_location):
        self.image = pygame.image.load(file_location)
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))