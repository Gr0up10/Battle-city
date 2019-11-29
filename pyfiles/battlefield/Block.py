import pygame

block_size = 50


class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y,is_wall=False):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image_path
        if image_path[15] in ('4','9','a','b','c', 's'):
            self.image = pygame.transform.scale(pygame.image.load(image_path), (block_size, block_size))
        elif image_path[15] in ('1','3','8','6'):
            self.image = pygame.transform.scale(pygame.image.load(image_path), (block_size, block_size//2))
        else:
            self.image = pygame.transform.scale(pygame.image.load(image_path), (block_size//2, block_size))
        #self.image = pygame.Surface((block_size, block_size)) #убрать, когда нужно будет накладывать текстуры
        #self.image.fill((255,0,0))                            # убрать, когда нужно будет накладывать текстуры
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_wall = is_wall

    def update(self):
        pass
        # тут будет реализована разрушаемость
