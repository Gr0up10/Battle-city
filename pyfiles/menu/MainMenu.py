import pygame
import sys


class MainMenu:
    def __init__(self):
        self.size = 800, 600
        self.colors = {"red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255),
                       "white": (255, 255, 255),
                       "black": (0, 0, 0),
                       "brown": (153, 76, 0),
                       "grey": (100, 100, 100)}
        self.integ = 0
        self.tank_imag = pygame.image.load('sprites/tank_for_menu.jpg')
        self.tank_rect = self.tank_imag.get_rect()
        self.tank_rect.x = 150
        self.tank_rect.y = 155
        self.ra = 150
        self.screen = pygame.display.set_mode(self.size)

    def show(self):
        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode(self.size)
        # текст на кнопках
        font = pygame.font.SysFont('Comic Sans MS', 45, True)
        data1 = '1 player'
        data2 = '2 players'
        data3 = 'custom map'
        data0 = 'Есть пробитие!'
        # --------------
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                elif event.type == pygame.KEYDOWN:

                    if chr(event.key) == 'w' or event.key == pygame.K_UP:
                        self.integ -= 1
                    elif chr(event.key) == 's' or event.key == pygame.K_DOWN:
                        self.integ += 1

                    if self.integ > 2:
                        self.integ = 0
                    elif self.integ < 0:
                        self.integ = 2
                    if self.integ == 0:
                        self.tank_rect.y = 155
                    elif self.integ == 1:
                        self.tank_rect.y = 305
                    elif self.integ == 2:
                        self.tank_rect.y = 455

                    if event.key == 32 or event.key == pygame.K_RETURN:
                        if self.integ == 0:
                            return 1
                        if self.integ == 1:
                            return 2
                    # блок для функций
            # if integ == 0 and chr(event.key) == 'space' or chr(event.key) == 'enter':
            #      onePlayerGame() # 1 игрок
            #   elif integ == 1 and chr(event.key) == 'space' or chr(event.key) == 'enter':
            #        twoPlayerGame() # 2 игрока
            #     elif integ == 2 and chr(event.key) == 'space' or chr(event.key) == 'enter':
            #          createCustomMap() # кастомную карту

            screen.fill(self.colors["black"])

            ts1 = font.render(data1, False, self.colors["white"])
            screen.blit(ts1, (300, self.ra + 10))
            ts2 = font.render(data2, False, self.colors["white"])
            screen.blit(ts2, (300, self.ra * 2 + 10))
            ts3 = font.render(data3, False, self.colors["white"])
            screen.blit(ts3, (300, self.ra * 3 + 10))

            ts0 = font.render(data0, False, self.colors["white"])  # главный текст пробития
            screen.blit(ts0, (280, 50))

            screen.blit(self.tank_imag, self.tank_rect)

            for i in range(3):
                pygame.draw.rect(screen, self.colors["white"], (200, (i + 1) * self.ra, 400, 50), 2)

            pygame.display.flip()
            pygame.time.wait(10)

        sys.exit(0)
