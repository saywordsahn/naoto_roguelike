import pygame
import random as rand
from world import World
from enemies import *
from items import *
from settings import *
from player import Player

pygame.init()



screen = pygame.display.set_mode((WIDTH, HEIGHT))



wall = pygame.image.load('dungeon/Tiles/tile_0037.png')
wall = pygame.transform.scale(wall, (64, 64))

armor = pygame.image.load('dungeon/Tiles/tile_0102.png')
armor = pygame.transform.scale(armor, (64, 64))

sword = pygame.image.load('dungeon/Tiles/tile_0103.png')
sword = pygame.transform.scale(armor, (64, 64))

# top_inside = pygame.image.load('dungeon/Tiles/tile_0002.png')
# top_inside = pygame.transform.scale(dirt, (64, 64))
#
# top_left = pygame.image.load('dungeon/Tiles/tile_0004.png')
# top_left = pygame.transform.scale(dirt, (64, 64))
#
# top_right = pygame.image.load('dungeon/Tiles/tile_0005.png')
# top_right = pygame.transform.scale(dirt, (64, 64))



player_armor1 = pygame.image.load('dungeon/Tiles/tile_0085.png')
player_armor1 = pygame.transform.scale(player_armor1, (64, 64))

player_armor2 = pygame.image.load('dungeon/Tiles/tile_0098.png')
player_armor2 = pygame.transform.scale(player_armor2, (64, 64))

player_armor3 = pygame.image.load('dungeon/Tiles/tile_0097.png')
player_armor3 = pygame.transform.scale(player_armor3, (64, 64))

player_armor4 = pygame.image.load('dungeon/Tiles/tile_0096.png')
player_armor4 = pygame.transform.scale(player_armor4, (64, 64))






class Student:

    def __init__(self, name):
        self.name = name




# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 50
# player_sprite.rect.bottom = 50
# player_speed = 8




player = Player()

rat = Rat()
spider = Spider()

armor = Armor (50, 50)
sword = Sword(75, 75)
health_pot = HealthPot(300, 75)
game_world = World()


while True:
    screen.fill(0)

    game_world.draw_tiles(screen)
    game_world.draw_enemies(screen)
    screen.blit(player.image, player.position)


    # screen.blit(player_armor1, (300, 300))
    # screen.blit(player_armor2, (300, 350))
    # screen.blit(player_armor3, (300, 400))
    # screen.blit(player_armor4, (300, 400))

    # enemies


    # items
    armor.draw(screen)
    sword.draw(screen)
    health_pot.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            player.move_right()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player.move_left()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.move_up()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            player.move_down()


    pygame.display.update()




clock = pygame.time.Clock()
FPS = 60


pygame.display.set_caption('Space Invaders')

bg = pygame.image.load('img/bg.png')

# player
player_image = pygame.image.load('img/spaceship.png')
player_sprite = pygame.sprite.Sprite()
player_sprite.image = player_image
player_sprite.rect = player_image.get_rect()
player_sprite.rect.centerx = 300
player_sprite.rect.bottom = 760
player_speed = 8


player_group = pygame.sprite.Group(player_sprite)


while True:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_sprite.rect.left > 0:
        player_sprite.rect.x -= player_speed

    if keys[pygame.K_RIGHT] and player_sprite.rect.right < screen_width:
        player_sprite.rect.x += player_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.blit(bg, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)