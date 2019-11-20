import pygame
import sys
from playerTank import PlayerTank
from field import Field

size = width, height = 800, 600
black = 0, 0, 0


def game_test_loop():
    DEBUG = 0
    pygame.init()
    screen = pygame.display.set_mode(size)
    tank = PlayerTank(screen)
    field = Field('level_1', screen)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                tank.keyEventDown(event.key)
                DEBUG = event.key
            elif event.type == pygame.KEYUP:
                tank.keyEventUp(event.key)

        # tank.check_collisions(field.blocks)
        screen.fill(black)

        # Код отрисовки пишется здесь
        field.draw_logic()
        tank.draw(screen)
        tank.move()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    game_test_loop()
