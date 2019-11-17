import pygame


class Field:

    def __init__(self, level_path, screen):  # level - путь до файла с уровнем
        self.screen = screen
        self.level_path = level_path
        self.level = list()

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
            cell = Cell('sprites/' + char + '.png', x, y)
            self.screen.blit(cell.image, cell.rect)


class Cell:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


size = width, height = 1000, 800
black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    is_close = False
    while not is_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_close = True

        field = Field('level_1', screen)
        screen.fill(black)
        field.draw_all()

        pygame.display.flip()  # double buffering
        pygame.time.wait(3)  # подождать 3 миллисекунд


if __name__ == '__main__':
    main()
