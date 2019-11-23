import pygame
from pyfiles.tanks.Tank import Tank


class Player1Tank(Tank):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = pygame.image.load('sprites/tanks/players/up.png')

    def update(self):
        self.deltaX = 0
        self.deltaY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.move_left()
            self.image = pygame.image.load('sprites/tanks/players/left.png')
        elif keystate[pygame.K_d]:
            self.move_right()
            self.image = pygame.image.load('sprites/tanks/players/right.png')
        elif keystate[pygame.K_w]:
            self.move_up()
            self.image = pygame.image.load('sprites/tanks/players/up.png')
        elif keystate[pygame.K_s]:
            self.move_down()
            self.image = pygame.image.load('sprites/tanks/players/down.png')
        if keystate[pygame.K_SPACE]:
            if not self.bullet_exist():
                self.shoot()
        self.check_collisions()