import pygame

from block2 import Block2


block_size = 50


class field2:
    def __init__(self, level_path='level_1.txt'):
        self.blocks = list()

        self.level_path = level_path
        self.level = list()
        self.level_init()

        self.blocks_init()

    def level_init(self):
        print('DEBUG1')
        # читаем уровень из файла и сохраняем его в level
        with open(self.level_path, 'r') as level_file:
            self.level = level_file.read().splitlines()
        print(self.level)

    def blocks_init(self):
        y = 0
        for string in self.level:
            x = 0
            for char in string:
                if char != 'd':
                    img_path = 'sprites/blocks/' + char + '.png'
                    self.blocks.append(Block2(img_path, x * block_size, y * block_size))
                x += 1
            y += 1
