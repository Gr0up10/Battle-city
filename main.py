import pygame
import sys
from field import Field
from tank import Tank

size = width, height = 800, 600
black = 0, 0, 0


def game_test_loop():
    screen = pygame.display.set_mode(size)
    tank = Tank(screen)
    field = Field('level_1', screen)
    pygame.init()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                tank.key_event_down(event)
            elif event.type == pygame.KEYUP:
                tank.key_event_up(event)

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
