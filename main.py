import pygame
import sys
import playerTank

size = width, height = 800, 600
black = 0, 0, 0


def game_test_loop():
    tank = playerTank()
    DEBUG = 0
    pygame.init()
    screen = pygame.display.set_mode(size)
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

        screen.fill(black)

        # Код отрисовки пишется здесь
        tank.draw(screen)
        fontObj = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = fontObj.render(str(DEBUG), True, (255, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 400)

        screen.blit(textSurfaceObj, textRectObj)

        tank.move()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    game_test_loop()
