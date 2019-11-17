import pygame
import sys

size = width, height = 800, 600
black = 0, 0, 0


class Tank():
    _tank_u = pygame.image.load("./Sprites/tank_u.png")
    _tank_d = pygame.image.load("./Sprites/tank_d.png")
    _tank_r = pygame.image.load("./Sprites/tank_r.png")
    _tank_l = pygame.image.load("./Sprites/tank_l.png")

    _move_right = False
    _move_left = False
    _move_up = False
    _move_down = False
    current_shift = 0

    tankrect = _tank_u.get_rect()
    tankrect.x = 100
    tankrect.y = 100

    tank_pic = _tank_r

    def __init__(self):
        pass

    def keyEventDown(self, event):
        if chr(event.key) == 'd':
            self.stop_moving()
            self._move_right = True
            self.current_shift = 1
        elif chr(event.key) == 'a':
            self.stop_moving()
            self._move_left = True
            self.current_shift = -1
        elif chr(event.key) == 'w':
            self.stop_moving()
            self._move_up = True
            self.current_shift = 1
        elif chr(event.key) == 's':
            self.stop_moving()
            self._move_down = True
            self.current_shift = -1

    def keyEventUp(self, event):
        if chr(event.key) == 'd':
            self._move_right = False
            self.current_shift = 0
        if chr(event.key) == 'a':
            self._move_left = False
            self.current_shift = 0
        if chr(event.key) == 'w':
            self._move_up = False
            self.current_shift = 0
        if chr(event.key) == 's':
            self._move_down = False
            self.current_shift = 0

    def draw(self, screen):
        screen.blit(self.tank_pic, self.tankrect)

    def move(self):
        if self._move_right:
            self.tank_pic = self._tank_r
            self.tankrect.x += 2
            self.tankrect.x += self.current_shift
        if self._move_left:
            self.tank_pic = self._tank_l
            self.tankrect.x -= 2
            self.tankrect.x += self.current_shift
        if self._move_up:
            self.tank_pic = self._tank_u
            self.tankrect.y -= 2
            self.tankrect.y += self.current_shift

        if self._move_down:
            self.tank_pic = self._tank_d
            self.tankrect.y += 2
            self.tankrect.y += self.current_shift
        self._check_collisions()

    def _check_collisions(self):
        if self.tankrect.x > width - 40:
            self.tankrect.x = width - 40
        if self.tankrect.y > height - 40:
            self.tankrect.y = height - 40
        if self.tankrect.x < 0:
            self.tankrect.x = 0
        if self.tankrect.y < 0:
            self.tankrect.y = 0

    def stop_moving(self):
        self._move_down = False
        self._move_left = False
        self._move_right = False
        self._move_left = False


def game_test_loop():
    tank = Tank()

    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                tank.keyEventDown(event)
            elif event.type == pygame.KEYUP:
                tank.keyEventUp(event)

        screen.fill(black)

        # Код отрисовки пишется здесь
        tank.draw(screen)

        tank.move()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    game_test_loop()
