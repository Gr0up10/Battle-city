import pygame
from Tank2 import Tank2


class Player1Tank2(Tank2):
    def __init__(self, sprites):
        super().__init__(sprites)

    def update(self):
        self.deltaX = 0
        self.deltaY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.move_left()
        if keystate[pygame.K_d]:
            self.move_right()
        if keystate[pygame.K_w]:
            self.move_up()
        if keystate[pygame.K_s]:
            self.move_down()
        if keystate[pygame.K_SPACE]:
            if not self.bullet_exist():
                self.shoot()
        self.check_collisions()