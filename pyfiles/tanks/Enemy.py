import pygame
import random
from pyfiles.tanks.Tank import Tank

WIDTH, HEIGHT = 800, 600


class Enemy(Tank):
    def __init__(self, sprites, bullets):
        super().__init__(sprites, bullets)
        self.rect.centerx = WIDTH / 2 - 150
        self.distance = 0
        self.cmd_choice = 0
        self.image = pygame.image.load('sprites/tank/tank_u.png')

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        if self.is_able_to_move is False:
            self.distance = 0
        self.choose_cmd()
        self.move()
        self.check_collisions()

    def move(self):
        if self.cmd_choice is not 4:
            print('moving')
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
        elif self.cmd_choice is 4:
            self.shoot()
            self.cmd_choice = 0     # остановка бага с бесконечной стрельбой

    def choose_cmd(self):
        if self.distance <= 0:
            self.cmd_choice = random.randint(0, 4)
            self.distance = 50 * random.randint(1, 5)

