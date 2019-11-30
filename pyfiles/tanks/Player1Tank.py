import pygame
from pyfiles.tanks.Tank import Tank

block_size = 40


class Player1Tank(Tank):
    def __init__(self, sprites, bullets):
        pic_u = pygame.transform.scale(pygame.image.load('sprites/tank/tank_u.png'), (block_size, block_size))
        pic_r = pygame.transform.scale(pygame.image.load('sprites/tank/tank_r.png'), (block_size, block_size))
        pic_d = pygame.transform.scale(pygame.image.load('sprites/tank/tank_d.png'), (block_size, block_size))
        pic_l = pygame.transform.scale(pygame.image.load('sprites/tank/tank_l.png'), (block_size, block_size))
        super().__init__(sprites, bullets, pic_u, pic_l, pic_d, pic_r)

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.move_left()
        elif keystate[pygame.K_d]:
            self.move_right()
        elif keystate[pygame.K_w]:
            self.move_up()
        elif keystate[pygame.K_s]:
            self.move_down()
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.check_collisions()
        self.set_sprite_picture()
