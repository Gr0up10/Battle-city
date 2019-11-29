import pygame
from pyfiles.tanks.Tank import Tank


class Player1Tank(Tank):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = pygame.image.load('sprites/tank/tank_u.png')

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.move_left()
            self.image = pygame.image.load('sprites/tank/tank_l.png')
        elif keystate[pygame.K_d]:
            self.move_right()
            self.image = pygame.image.load('sprites/tank/tank_r.png')
        elif keystate[pygame.K_w]:
            self.move_up()
            self.image = pygame.image.load('sprites/tank/tank_u.png')
        elif keystate[pygame.K_s]:
            self.move_down()
            self.image = pygame.image.load('sprites/tank/tank_d.png')
        if keystate[pygame.K_SPACE]:
            if not self.bullet_exist():
                self.shoot()
        self.check_collisions()
