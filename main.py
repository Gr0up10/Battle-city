import pygame
import sys

size = width, height = 800, 600
black = 0, 0, 0



def main():

    tank_u = pygame.image.load("tank_u.png")
    tank_d = pygame.image.load("tank_d.png")
    tank_r = pygame.image.load("tank_r.png")
    tank_l = pygame.image.load("tank_l.png")

    tankrect = tank_u.get_rect()
    tankrect.x = 100
    tankrect.y = 100

    move_right = False
    move_left = False
    move_up = False
    move_down = False
    current_shift = 0

    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if chr(event.key) == 'd':
                    move_right = True
                    current_shift = 1
                if chr(event.key) == 'a':
                    move_left = True
                    current_shift = -1
                if chr(event.key) == 'w':
                    move_up = True
                    current_shift = 1
                if chr(event.key) == 's':
                    move_down = True
                    current_shift = -1
            elif event.type == pygame.KEYUP:
                if chr(event.key) == 'd':
                    move_right = False
                    current_shift = 0
                if chr(event.key) == 'a':
                    move_left = False
                    current_shift = 0
                if chr(event.key) == 'w':
                    move_up = False
                    current_shift = 0
                if chr(event.key) == 's':
                    move_down = False
                    current_shift = 0

        screen.fill(black)

        # Код отрисовки пишется здесь
        screen.blit(tank_r, tankrect)

        if move_right:
            screen.blit(tank_r, tankrect)
            tankrect.x += 2
            tankrect.x += current_shift
        if move_left:
            screen.blit(tank_l, tankrect)
            tankrect.x -= 2
            tankrect.x += current_shift
        if move_up:
            screen.blit(tank_u, tankrect)
            tankrect.y -= 2
            tankrect.y += current_shift

        if move_down:
            screen.blit(tank_d, tankrect)
            tankrect.y += 2
            tankrect.y += current_shift

        if tankrect.x > width - 40:
            tankrect.x = width - 40
        if tankrect.y > height - 40:
            tankrect.y = height - 40
        if tankrect.x < 0:
            tankrect.x = 0
        if tankrect.y < 0:
            tankrect.y = 0


        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()

if __name__ == '__main__':
    main()
