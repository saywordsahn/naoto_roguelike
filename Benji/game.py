from settings import *


class Game:

    def __init__(self, world, player, ui):
        self.world = world
        self.player = player
        self.ui = ui

    def interact(self, direction):

        obj = self.world.get_adjacent_object(self.player.position, direction)

        if obj is not None:

            if obj.type == Type.ITEM:
                self.player.pick_up_item(obj)
                self.move_player(direction)
            elif obj.type == Type.ENEMY:
                obj.take_damage(self.player.attack_damage)
                if obj.hp <= 0:
                    self.world.remove_game_object(self.player.position, direction)
                    self.move_player(direction)
        else:
            self.move_player(direction)

        self.enemy_turn()

    def enemy_turn(self):

        for cell in self.world.get_cells_with_enemies():

            # TODO: attack player if adjacent
            enemy = cell.object

            if enemy.get_action() == EnemyBehavior.MOVE:

                direction = enemy.get_movement(cell.position, self.world, self.player.position)

                if direction is not None:
                    self.world.move_object(cell.position, direction)



    def move_player(self, direction):
        self.world.move_object(self.player.position, direction)
        self.player.move(direction)

    def draw(self, screen):
        self.world.draw_world(screen)
        self.ui.draw(screen)
