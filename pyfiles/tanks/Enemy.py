import pygame
import random
from pyfiles.tanks.Tank import Tank

WIDTH, HEIGHT = 800, 600
block_size = 40


class Enemy(Tank):
    def __init__(self, sprites, bullets):
        pic_u = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_u.png'), (block_size, block_size))
        pic_r = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_r.png'), (block_size, block_size))
        pic_d = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_d.png'), (block_size, block_size))
        pic_l = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_l.png'), (block_size, block_size))
        super().__init__(sprites, bullets, pic_u, pic_l, pic_d, pic_r)
        self.rect.centerx = 4*50 + 25
        self.rect.bottom = 140
        self.distance = 0
        self.cmd_choice = 0

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        if self.is_able_to_move is False:
            self.distance = 0
        self.choose_cmd()
        self.move()
        self.check_collisions()
        self.set_sprite_picture()

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
        elif self.cmd_choice is 4:
            self.shoot()
            self.cmd_choice = 0     # остановка бага с бесконечной стрельбой

    def choose_cmd(self):
        if self.distance <= 0:
            self.cmd_choice = random.randint(0, 4)
            self.distance = 50 * random.randint(1, 5)

