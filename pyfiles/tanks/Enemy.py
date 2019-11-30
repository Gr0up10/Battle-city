import pygame
import random
from pyfiles.tanks.Tank import Tank


class Enemy(Tank):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.distance = 0
        self.cmd_choice = 0
        self.image = pygame.image.load('sprites/tank/tank_u.png')

    def update(self):
        self.deltaX = 0
        self.deltaY = 0
        if self.is_able_to_move is False:
            self.distance = 0
        self.choose_cmd()
        self.move()
        self.check_collisions()

    def move(self):
        if self.cmd_choice is 0:
            self.distance -= self.speed
            self.move_up()
        elif self.cmd_choice is 1:
            self.distance -= self.speed
            self.move_right()
        elif self.cmd_choice is 2:
            self.distance -= self.speed
            self.move_down()
        elif self.cmd_choice is 3:
            self.distance -= self.speed
            self.move_left()

    def choose_cmd(self):
        if self.distance <= 0:
            self.cmd_choice = random.randint(0, 3)
            self.distance = 50 * random.randint(1, 5)
