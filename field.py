import pygame

from block import Block
from brick import Brick


class Field:

    def __init__(self, level_path, screen):  # level_path - путь до файла с уровнем
        self.blocks_d = dict()
        self.blocks = list()
        self.screen = screen
        self.level_path = level_path
        self.level = list()
        self.blocks_d_init()
        self.level_init()
        self.blocks_init()

    def blocks_d_init(self):
        self.blocks_d['0'] = Block('sprites/blocks/0.png', self.screen)
        self.blocks_d['1'] = Block('sprites/blocks/1.png', self.screen)
        self.blocks_d['2'] = Block('sprites/blocks/2.png', self.screen)
        self.blocks_d['3'] = Block('sprites/blocks/3.png', self.screen)
        self.blocks_d['4'] = Block('sprites/blocks/4.png', self.screen)
        self.blocks_d['5'] = Block('sprites/blocks/5.png', self.screen)
        self.blocks_d['6'] = Block('sprites/blocks/6.png', self.screen)
        self.blocks_d['7'] = Block('sprites/blocks/7.png', self.screen)
        self.blocks_d['8'] = Block('sprites/blocks/8.png', self.screen)
        self.blocks_d['9'] = Block('sprites/blocks/9.png', self.screen)
        self.blocks_d['a'] = Block('sprites/blocks/a.png', self.screen)
        self.blocks_d['b'] = Block('sprites/blocks/b.png', self.screen)
        self.blocks_d['c'] = Block('sprites/blocks/c.png', self.screen)
        self.blocks_d['d'] = Block('sprites/blocks/d.png', self.screen)

    def level_init(self):
        # читаем уровень из файла и сохраняем его в level
        with open(self.level_path, 'r') as level_file:
            self.level = level_file.read().splitlines()

    def blocks_init(self):
        for string in self.level:
            row = list()
            for char in string:
                row.append(self.blocks_d[char])
            self.blocks.append(list(row))

    def draw_logic(self):
        y = 0
        for row in self.blocks:
            x = 0
            for block in row:
                self.draw_block(block, x, y)
                x += 40
            y += 40

    def draw_block(self, block, x, y):
        if '/0.' in block.image_path or '/5.' in block.image_path:
            block.draw(x + 20, y)
        elif '/1.' in block.image_path or '/6.' in block.image_path:
            block.draw(x, y + 20)
        else:
            block.draw(x, y)
