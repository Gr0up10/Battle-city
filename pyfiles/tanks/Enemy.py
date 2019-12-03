import pygame
import random
from pyfiles.tanks.Tank import Tank
from pyfiles.tanks.Bullet import Bullet

WIDTH, HEIGHT = 800, 600
block_size = 40


class Enemy(Tank):
    def __init__(self, sprites, bullets,x,y):
        pic_u = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_u.png'), (block_size, block_size))
        pic_r = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_r.png'), (block_size, block_size))
        pic_d = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_d.png'), (block_size, block_size))
        pic_l = pygame.transform.scale(pygame.image.load('sprites/enemy1/enemy_l.png'), (block_size, block_size))
        super().__init__(sprites, bullets, pic_u, pic_l, pic_d, pic_r)
        self.rect.centerx = x
        self.rect.bottom = y
        self.distance = 0
        self.cmd_choice = 0

    def shoot(self):
        if self.shooting_cooldown == 0:
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
            self.sprites.add(bullet)
            self.shooting_cooldown = 50
            self.bullets.append(bullet)

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        self.choose_cmd()
        # выбирает стрелять или нет. Шанс 1 к 11
        if self.cmd_choice is 1:
            self.shoot()
        self.move()
        self.check_collisions()
        self.set_sprite_picture()

    def move(self):
        if self.is_able_to_move is False:
            self.distance = 0
        self.choose_direction()
        if self.direction is 0:
            self.distance -= self.speed
            self.move_up()
        elif self.direction is 1:
            self.distance -= self.speed
            self.move_right()
        elif self.direction is 2:
            self.distance -= self.speed
            self.move_down()
        elif self.direction is 3:
            self.distance -= self.speed
            self.move_left()

    def choose_direction(self):
        if self.distance <= 0:
            self.direction = random.randint(0, 3)
            self.distance = 50 * random.randint(1, 2)

    def choose_cmd(self):
        # if self.distance <= 0:
        self.cmd_choice = random.randint(1, 11)
