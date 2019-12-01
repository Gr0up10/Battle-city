import pygame
from pyfiles.battlefield.Block import Block

block_size = 50


class Brick(Block):
    # images
    quarter = pygame.transform.scale(pygame.image.load('sprites/blocks/4.png'), (block_size // 2, block_size // 2))
    half = pygame.transform.scale(pygame.image.load('sprites/blocks/1.png'), (block_size, block_size // 2))
    # halflaying = pygame.transform.scale(pygame.image.load('sprites/blocks/2.png'), (block_size // 2, block_size // 2))
    full = pygame.transform.scale(pygame.image.load('sprites/blocks/4.png'), (block_size, block_size))

    def __init__(self, image_path, x, y, hp):
        super().__init__(image_path, x, y)
        self.hp = hp
        self.set_image()
        self.rect = self.image.get_rect()
        self.current_x = x
        self.current_y = y
        self.rect.x = self.current_x
        self.rect.y = self.current_y

    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.current_x
        self.rect.y = self.current_y

    def set_image(self):
        if self.hp == 1:
            self.image = self.quarter
        elif self.hp == 2:
            self.image = self.half
        elif self.hp == 3:
            self.image = self.full

    def damage(self):
        print('brick was damaged')
        self.hp -= 1
        if self.hp == 0:
            print('brick was destroyed')
            self.kill()
        elif self.hp == 1:
            # correct cords
            pass
        elif self.hp == 2:
            # correct cords
            pass
        elif self.hp == 3:
            # correct cords
            pass
        self.set_image()
        self.update_rect()
