import random as rand

class World:

    def __init__(self, num_rows, num_cols):
        self.rows = num_rows
        self.cols = num_cols
        self.world = []
        self.generate_world()

    def generate_world(self):

        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                r = rand.randint(0, 100)
                if r < 10:
                    row.append(rocks)
                else:
                    row.append(dirt)

            self.world.append(row)

    def draw_world(self):
        for i in range(self.rows):
            for j in range(self.cols):
                screen.blit(self.world[i][j], (j * CELL_SIZE, i * CELL_SIZE))