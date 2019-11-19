import pygame

from cell import Cell


class Field:
    blocks = dict()

    def __init__(self, level_path, screen):  # level - путь до файла с уровнем
        self.screen = screen
        self.level_path = level_path
        self.level = list()
        self.cells_init()
        self.level_init()

    def cells_init(self):
        self.blocks['0'] = Cell('sprites/blocks/0.png', self.screen)
        self.blocks['1'] = Cell('sprites/blocks/1.png', self.screen)
        self.blocks['2'] = Cell('sprites/blocks/2.png', self.screen)
        self.blocks['3'] = Cell('sprites/blocks/3.png', self.screen)
        self.blocks['4'] = Cell('sprites/blocks/4.png', self.screen)
        self.blocks['5'] = Cell('sprites/blocks/5.png', self.screen)
        self.blocks['6'] = Cell('sprites/blocks/6.png', self.screen)
        self.blocks['7'] = Cell('sprites/blocks/7.png', self.screen)
        self.blocks['8'] = Cell('sprites/blocks/8.png', self.screen)
        self.blocks['9'] = Cell('sprites/blocks/9.png', self.screen)
        self.blocks['a'] = Cell('sprites/blocks/a.png', self.screen)
        self.blocks['b'] = Cell('sprites/blocks/b.png', self.screen)
        self.blocks['c'] = Cell('sprites/blocks/c.png', self.screen)

    def level_init(self):
        # читаем уровень из файла и сохраняем его в level
        with open(self.level_path, 'r') as level_file:
            self.level = level_file.read().splitlines()

    def draw_all(self):
        y = 0
        for string in self.level:
            x = 0
            for char in string:
                self.draw_cell(char, x, y)
                x += 40
            y += 40

    def draw_cell(self, char, x, y):
        # отрисовка клетки. Имя фотографии == значению char
        if char != 'd':
            if char in '05':
                self.blocks[char].draw(x + 20, y)
            elif char in '16':
                self.blocks[char].draw(x, y + 20)
            else:
                self.blocks[char].draw(x, y)


size = width, height = 1000, 800
black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    is_close = False
    field = Field('level_1', screen)
    while not is_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_close = True

        screen.fill(black)
        field.draw_all()

        pygame.display.flip()  # double buffering
        pygame.time.wait(3)  # подождать 3 миллисекунд


if __name__ == '__main__':
    main()
