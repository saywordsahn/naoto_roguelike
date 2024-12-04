import pygame
import random as rand

pygame.init()




NUM_ROWS = 12
NUM_COLS = 12
CELL_SIZE = 64
WIDTH = CELL_SIZE * NUM_COLS
HEIGHT = CELL_SIZE * NUM_ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))

dirt = pygame.image.load('dungeon/Tiles/tile_0000.png')
dirt = pygame.transform.scale(dirt, (64, 64))

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

rocks = pygame.image.load('dungeon/Tiles/tile_0024.png')
rocks = pygame.transform.scale(rocks, (64, 64))

player_armor1 = pygame.image.load('dungeon/Tiles/tile_0085.png')
player_armor1 = pygame.transform.scale(player_armor1, (64, 64))

player_armor2 = pygame.image.load('dungeon/Tiles/tile_0098.png')
player_armor2 = pygame.transform.scale(player_armor2, (64, 64))

player_armor3 = pygame.image.load('dungeon/Tiles/tile_0097.png')
player_armor3 = pygame.transform.scale(player_armor3, (64, 64))

player_armor4 = pygame.image.load('dungeon/Tiles/tile_0096.png')
player_armor4 = pygame.transform.scale(player_armor4, (64, 64))

class Bat:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0120.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

class Player:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0088.png')

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



player = Player()
bat = Bat(500, 500)
game_world = World()

# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 50
# player_sprite.rect.bottom = 50
# player_speed = 8







while True:
    screen.fill(0)

    game_world.draw_world()
    screen.blit(player.image, player.position)
    screen.blit(bat.image, bat.position)

    screen.blit(player_armor1, (300, 300))
    screen.blit(player_armor2, (300, 350))
    screen.blit(player_armor3, (300, 400))
    screen.blit(player_armor4, (300, 400))
    screen.blit(bat.image, bat.position)
    screen.blit(armor, (400, 300))


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