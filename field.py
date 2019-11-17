import pygame


class Field:
    cells = dict()

    def __init__(self, level_path, screen):  # level - путь до файла с уровнем
        self.screen = screen
        self.level_path = level_path
        self.level = list()
        self.cells_init()

    def cells_init(self):
        self.cells['0'] = Cell('sprites/blocks/0.png', self.screen)
        self.cells['1'] = Cell('sprites/blocks/1.png', self.screen)
        self.cells['2'] = Cell('sprites/blocks/2.png', self.screen)
        self.cells['3'] = Cell('sprites/blocks/3.png', self.screen)
        self.cells['4'] = Cell('sprites/blocks/4.png', self.screen)
        self.cells['5'] = Cell('sprites/blocks/5.png', self.screen)
        self.cells['6'] = Cell('sprites/blocks/6.png', self.screen)
        self.cells['7'] = Cell('sprites/blocks/7.png', self.screen)
        self.cells['8'] = Cell('sprites/blocks/8.png', self.screen)
        self.cells['9'] = Cell('sprites/blocks/9.png', self.screen)
        self.cells['a'] = Cell('sprites/blocks/a.png', self.screen)
        self.cells['b'] = Cell('sprites/blocks/b.png', self.screen)
        self.cells['c'] = Cell('sprites/blocks/c.png', self.screen)

    def draw_all(self):
        with open(self.level_path, 'r') as level_file:
            # читаем уровень из файла и сохраняем его в level
            self.level = level_file.read().splitlines()
            y = 0
            for string in self.level:
                x = 0
                for char in string:
                    self.draw_cell(char, x, y)
                    x += 40
                y += 40

    def draw_cell(self, char, x, y):
        # отрисовка клетки.  Имя фотографии == значению char
        if char != 'd':
            if char in '05':
                self.cells[char].draw(x + 20, y)
            elif char in '05':
                self.cells[char].draw(x + 20, y)
            elif char in '16':
                self.cells[char].draw(x, y + 20)
            else:
                self.cells[char].draw(x, y)


class Cell:
    def __init__(self, image_path, screen):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image, self.rect)


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
