import pygame


class Block(pygame.sprite.Sprite):
    bs = 50

    # состояние блока
    f = 'full'
    t, r, b, l = 'top', 'right', 'bottom', 'left'
    tl, tr, bl, br = 'top_left', 'top_right', 'bottom_left', 'bottom_right'

    standing = pygame.transform.scale(pygame.image.load('sprites/blocks/void.png'), (bs // 2, bs))
    lying = pygame.transform.scale(pygame.image.load('sprites/blocks/void.png'), (bs, bs // 2))
    full = pygame.transform.scale(pygame.image.load('sprites/blocks/void.png'), (bs, bs))
    quarter = pygame.transform.scale(pygame.image.load('sprites/blocks/void.png'), (bs // 2, bs // 2))

    def __init__(self, x, y, state='full'):
        pygame.sprite.Sprite.__init__(self)
        self.state = state
        self.hp = 3
        # исходные координаты блока. Без поправки на состояние
        self.source_x = x
        self.source_y = y
        # текущие координаты блока.
        self.current_x = x
        self.current_y = y

        self.image = self.full
        self.rect = self.image.get_rect()
        self.rect.x = self.current_x
        self.rect.y = self.current_y
        self.hp_init()
        self.set_image()
        self.correct_cords()
        self.update_rect()

    def hp_init(self):
        if self.state == self.f:
            self.hp = 3
        elif self.state == self.l or self.state == self.r or self.state == self.t or self.state == self.b:
            self.hp = 2
        else:
            self.hp = 1

    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.current_x
        self.rect.y = self.current_y

    def set_image(self):
        # задает изображение в соответствии с состоянием блока
        if self.state == self.f:
            self.image = self.full
        elif self.state == self.t or self.state == self.b:
            self.image = self.lying
        elif self.state == self.r or self.state == self.l:
            self.image = self.standing
        elif self.state == self.tl or \
                self.state == self.tr or \
                self.state == self.bl or \
                self.state == self.br:
            self.image = self.quarter

    def correct_cords(self):
        if self.state == self.r or self.state == self.tr:
            self.current_x = self.source_x + self.bs // 2
        elif self.state == self.b or self.state == self.bl:
            self.current_y = self.source_y + self.bs // 2
        elif self.state == self.br:
            self.current_y = self.source_y + self.bs // 2
            self.current_x = self.source_x + self.bs // 2
