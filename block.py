import pygame


class Block:
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

    def collision(self):
        pass

    def is_wall(self):
        return False
