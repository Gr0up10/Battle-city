import pygame

block_size = 50


class Block2(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y,is_wall=False):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image_path
        #self.image = pygame.image.load(image_path)           # раскомментировать, когда нужно будет накладывать текстуры
        self.image = pygame.Surface((block_size, block_size)) #убрать, когда нужно будет накладывать текстуры
        self.image.fill((255,0,0))                            # убрать, когда нужно будет накладывать текстуры
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_wall = is_wall

    def update(self):
        pass
        # тут будет реализована разрушаемость
