import pygame

size = width, height = 800, 600

class Tank:
    def __init__(self, screen):
        self.screen = screen
        self._tank_u = pygame.image.load("sprites/tank/tank_u.png")
        self._tank_d = pygame.image.load("sprites/tank/tank_d.png")
        self._tank_r = pygame.image.load("sprites/tank/tank_r.png")
        self._tank_l = pygame.image.load("sprites/tank/tank_l.png")

        self._move_right = False
        self._move_left = False
        self._move_up = False
        self._move_down = False
        self.current_shift = 2

        self.tankrect = self._tank_u.get_rect()
        self.tankrect.x = 100
        self.tankrect.y = 100

        self.tank_pic = self._tank_r

    def _go_left(self):
        self.stop_moving()
        self._move_left = True
        self.current_shift = -1

    def _go_right(self):
        self.stop_moving()
        self._move_right = True
        self.current_shift = 1

    def _go_down(self):
        self.stop_moving()
        self._move_down = True
        self.current_shift = -1

    def _go_up(self):
        self.stop_moving()
        self._move_up = True
        self.current_shift = 1

    def _stop_moving_right(self):
        self._move_right = False
        self.current_shift = 0

    def _stop_moving_left(self):
        self._move_left = False
        self.current_shift = 0

    def _stop_moving_up(self):
        self._move_up = False
        self.current_shift = 0

    def _stop_moving_down(self):
        self._move_down = False
        self.current_shift = 0

    def _stop_moving(self):
        self._move_right = False
        self._move_left = False
        self._move_up = False
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


    def collision(self, block):
        if block.is_wall:
            print('collision tank and block')

    def stop_moving(self):
        self._move_down = False
        self._move_left = False
        self._move_right = False
        self._move_left = False

    def current_state(self):
        if self._move_right:
            return 1
        if self._move_up:
            return 2
        if self._move_left:
            return 3
        if self._move_down:
            return 4
