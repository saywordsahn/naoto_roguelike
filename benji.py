import pygame
import random as rand

pygame.init()




NUM_ROWS = 12
NUM_COLS = 12
CELL_SIZE = 64
WIDTH = CELL_SIZE * NUM_COLS
HEIGHT = CELL_SIZE * NUM_ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))



wall = pygame.image.load('dungeon/Tiles/tile_0037.png')
wall = pygame.transform.scale(wall, (64, 64))



sword = pygame.image.load('dungeon/Tiles/tile_0103.png')
sword = pygame.transform.scale(sword, (64, 64))

# top_inside = pygame.image.load('dungeon/Tiles/tile_0002.png')
# top_inside = pygame.transform.scale(dirt, (64, 64))
#
# top_left = pygame.image.load('dungeon/Tiles/tile_0004.png')
# top_left = pygame.transform.scale(dirt, (64, 64))
#
# top_right = pygame.image.load('dungeon/Tiles/tile_0005.png')
# top_right = pygame.transform.scale(dirt, (64, 64))





class Bat:

    def __init__(self, x, y):
        self.image = pygame.image.load('dungeon/Tiles/tile_0120.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.position = (x, y)

class Armor:

    def __init__(self):
        self.image = pygame.image.load('dungeon/Tiles/tile_0102.png')
        self.image = pygame.transform.scale(self.image, (64, 64))

class Player:

    def __init__(self):
        player_armor0 = pygame.image.load('dungeon/Tiles/tile_0088.png')
        player_armor0 = pygame.transform.scale(player_armor0, (64, 64))

        player_armor1 = pygame.image.load('dungeon/Tiles/tile_0085.png')
        player_armor1 = pygame.transform.scale(player_armor1, (64, 64))

        player_armor2 = pygame.image.load('dungeon/Tiles/tile_0098.png')
        player_armor2 = pygame.transform.scale(player_armor2, (64, 64))

        player_armor3 = pygame.image.load('dungeon/Tiles/tile_0097.png')
        player_armor3 = pygame.transform.scale(player_armor3, (64, 64))

        player_armor4 = pygame.image.load('dungeon/Tiles/tile_0096.png')
        player_armor4 = pygame.transform.scale(player_armor4, (64, 64))
        self.images = []
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

class World:

    def __init__(self):
        self.rows = 12
        self.cols = 12
        self.world = []
        self.empty_tiles = []
        self.item_map = [[None for i in range(self.cols)] for j in range(self.rows)]

        self.dirt = pygame.image.load('dungeon/Tiles/tile_0000.png')
        self.dirt = pygame.transform.scale(self.dirt, (64, 64))

        self.rocks = pygame.image.load('dungeon/Tiles/tile_0024.png')
        self.rocks = pygame.transform.scale(self.rocks, (64, 64))

    def get_coords(self, x, y):
        return x * CELL_SIZE, y * CELL_SIZE

    def generate_items(self):

        for i in range(rand.randint(3, 5)):
            random_cell = rand.choice(self.empty_tiles)
            self.empty_tiles.remove(random_cell)
            armor = Armor()
            self.item_map[random_cell[0]][random_cell[1]] = armor


    def generate_world(self):

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                r = rand.randint(0, 100)
                if r < 10:
                    row.append(self.rocks)
                else:
                    row.append(self.dirt)

                self.empty_tiles.append((i, j))
            self.world.append(row)

        self.generate_items()

    def draw_world(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                screen.blit(self.world[i][j], (j * CELL_SIZE, i * CELL_SIZE))

                if self.item_map[i][j] is not None:
                    screen.blit(self.item_map[i][j].image, (j * CELL_SIZE, i * CELL_SIZE))




player = Player()
bat = Bat(500, 500)

# player_sprite = pygame.sprite.Sprite()
# player_sprite.image = player_image
# player_sprite.rect = player_image.get_rect()
# player_sprite.rect.centerx = 50
# player_sprite.rect.bottom = 50
# player_speed = 8






game_world = World()
game_world.generate_world()


while True:
    screen.fill(0)

    game_world.draw_world(screen)
    screen.blit(player.image, player.position)
    screen.blit(bat.image, bat.position)

    screen.blit(player_armor1, (300, 300))
    screen.blit(player_armor2, (300, 350))
    screen.blit(player_armor3, (300, 400))
    screen.blit(player_armor4, (300, 400))
    screen.blit(bat.image, bat.position)



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