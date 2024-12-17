import pygame
import random as rand
from settings import *
from enemies import *
from player import *
from world import *

pygame.init()


# NUM_ROWS = 12
# NUM_COLS = 12
# CELL_SIZE = 64
WIDTH = CELL_SIZE * NUM_COLS
HEIGHT = CELL_SIZE * NUM_ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))






sword = pygame.image.load('../dungeon/Tiles/tile_0103.png')
sword = pygame.transform.scale(sword, (64, 64))

# top_inside = pygame.image.load('dungeon/Tiles/tile_0002.png')
# top_inside = pygame.transform.scale(dirt, (64, 64))
#
# top_left = pygame.image.load('dungeon/Tiles/tile_0004.png')
# top_left = pygame.transform.scale(dirt, (64, 64))
#
# top_right = pygame.image.load('dungeon/Tiles/tile_0005.png')
# top_right = pygame.transform.scale(dirt, (64, 64))
















player = Player()
bat = Bat()

# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 50
# player_sprite.rect.bottom = 50
# player_speed = 8



class Game:

    def __init__(self, world, player):
        self.world = world
        self.player = player

    def interact(self, direction):
        print('player tries to interact with ', direction)
        pass

game_world = World()
game_world.generate_world()

game_world.add_object_to_cell(player, 1, 1)

game = Game(game_world, player)



while True:
    screen.fill(0)

    game_world.draw_world(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            game.interact(Direction.RIGHT)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            game.interact(Direction.LEFT)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            game.interact(Direction.UP)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            game.interact(Direction.DOWN)


    pygame.display.update()


#
#
# clock = pygame.time.Clock()
# FPS = 60
#
#
# pygame.display.set_caption('Space Invaders')
#
# bg = pygame.image.load('img/bg.png')
#
# # player
# player_image = pygame.image.load('img/spaceship.png')
# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 300
# player_sprite.rect.bottom = 760
# player_speed = 8
#
#
# player_group = pygame.sprite.Group(player_sprite)
#
#
# while True:
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT] and player_sprite.rect.left > 0:
#         player_sprite.rect.x -= player_speed
#
#     if keys[pygame.K_RIGHT] and player_sprite.rect.right < screen_width:
#         player_sprite.rect.x += player_speed
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit(0)
#
#     screen.blit(bg, (0, 0))
#     player_group.draw(screen)
#     pygame.display.update()
#     clock.tick(FPS)