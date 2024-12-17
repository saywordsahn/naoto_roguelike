import pygame

class Player:

    def __init__(self):
        player_armor0 = pygame.image.load('../dungeon/Tiles/tile_0088.png')
        player_armor0 = pygame.transform.scale(player_armor0, (64, 64))

        player_armor1 = pygame.image.load('../dungeon/Tiles/tile_0085.png')
        player_armor1 = pygame.transform.scale(player_armor1, (64, 64))

        player_armor2 = pygame.image.load('../dungeon/Tiles/tile_0098.png')
        player_armor2 = pygame.transform.scale(player_armor2, (64, 64))

        player_armor3 = pygame.image.load('../dungeon/Tiles/tile_0097.png')
        player_armor3 = pygame.transform.scale(player_armor3, (64, 64))

        player_armor4 = pygame.image.load('../dungeon/Tiles/tile_0096.png')
        player_armor4 = pygame.transform.scale(player_armor4, (64, 64))
        self.images = [player_armor0, player_armor1, player_armor2, player_armor3,
                       player_armor4]
        self.image = self.images[0]

        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (0, 0)

    def move_right(self):
        self.position = (self.position[0] + 64, self.position[1])

    def move_left(self):
        self.position = (self.position[0] - 64, self.position[1])

    def move_up(self):
        self.position = (self.position[0], self.position[1] - 64)

    def move_down(self):
        self.position = (self.position[0], self.position[1] + 64)

    def draw(self, screen):
        screen.blit(self.image, self.position)
