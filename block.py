import pygame


class Block:
    def __init__(self, image_path, screen, is_wall=False):
        self.screen = screen
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.is_wall = is_wall

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image, self.rect)

    def collision(self):
        pass

    def collides_with(self):
        pass
