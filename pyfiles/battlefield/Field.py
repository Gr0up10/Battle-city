import pygame

from pyfiles.battlefield.Block import Block


block_size = 50


class Field:
    #группа разрушаемых блоков
    bricks = pygame.sprite.Group()
    #группа неразрушаемых
    unbreakable = pygame.sprite.Group()
    #группа для кустов
    plants = pygame.sprite.Group()
    #группа для воды
    water = pygame.sprite.Group()
    
    def __init__(self, level_path='levels/level_1.txt'):
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
                    if char in ('0','1','2','3','4','s'):
                        self.bricks.add(Block(img_path, x * block_size, y * block_size))
                    elif char in ('9','5','6','7','8','c'):
                        self.unbreakable.add(Block(img_path, x * block_size, y * block_size))
                    elif char == 'b':
                        self.plants.add(Block(img_path, x * block_size, y * block_size))
                    elif char == 'a':
                        self.water.add(Block(img_path, x * block_size, y * block_size))
                x += 1
            y += 1

    def init_field_sprites_group(self):
        field_sprites = pygame.sprite.Group()
        for b in self.bricks:
            field_sprites.add(b)
        for b in self.unbreakable:
            field_sprites.add(b)
        for b in self.water:
            field_sprites.add(b)
        return field_sprites
