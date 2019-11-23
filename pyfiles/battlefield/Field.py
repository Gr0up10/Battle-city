import pygame

from pyfiles.battlefield.Block import Block


block_size = 50


class Field:
    #группа разрушаемых блоков
    bricks = pygame.sprite.Group()
    
    def __init__(self, level_path='levels/level_1.txt'):
        self.blocks = list()
        self.level_path = level_path
        self.level = list()
        self.level_init()
        self.blocks_init()

    def level_init(self):
        # читаем уровень из файла и сохраняем его в level
        with open(self.level_path, 'r') as level_file:
            self.level = level_file.read().splitlines()

    def blocks_init(self):
        y = 0
        for string in self.level:
            x = 0
            for char in string:
                if char != 'd':
                    img_path = 'sprites/blocks/' + char + '.png'
                    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4':
                        self.bricks.add(Block(img_path, x * block_size, y * block_size))
                    self.blocks.append(Block(img_path, x * block_size, y * block_size))
                x += 1
            y += 1
