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

rocks = pygame.image.load('dungeon/Tiles/tile_0024.png')
rocks = pygame.transform.scale(rocks, (64, 64))


player_image = pygame.image.load('dungeon/Tiles/tile_0088.png')
player_image = pygame.transform.scale(player_image, (64, 64))
x = 50
y = 50
# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 50
# player_sprite.rect.bottom = 50
# player_speed = 8
game_world = []

def generate_world():

    for i in range(NUM_ROWS):
        row = []
        for j in range(NUM_COLS):
            r = rand.randint(0, 100)
            if r < 10:
                row.append(rocks)
            else:
                row.append(dirt)

        game_world.append(row)



def draw_world():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            screen.blit(game_world[i][j], (j * CELL_SIZE, i * CELL_SIZE))



generate_world()

while True:
    screen.fill(0)

    draw_world()
    screen.blit(player_image, (x, y))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


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