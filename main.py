import pygame
import sys
from pyfiles.tanks.Player1Tank import Player1Tank
from pyfiles.battlefield.Field import Field
from pyfiles.MainMenu import MainMenu
size = width, height = 800, 600
black = 0, 0, 0
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 800, 600


def one_player_loop():
    all_sprites = pygame.sprite.Group()  # объявляем группы спрайтов
    field_sprites = pygame.sprite.Group()

    pygame.init()
    screen = pygame.display.set_mode(size)  # инициализация pygame

    f = field2()                            # инициализация поля, загрузка в field_sprites
    for b in f.blocks:
        field_sprites.add(b)

    player = Player1Tank2(all_sprites)  # инициализация танка игрока

    all_sprites.add(player)             # загрузка танка игрока

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Обновление
        all_sprites.update()
        field_sprites.update()

        screen.fill(black)

        # Код отрисовки пишется здесь
        field_sprites.draw(screen)
        all_sprites.draw(screen)

        # коллизия танка со стенами
        if pygame.sprite.spritecollideany(player, field_sprites):
            print('collision')
            player.is_able_to_move = False
            
        # коллизия снаряда с кирпичным блоком
        if player.bullet_exist():
            if pygame.sprite.spritecollideany(player.bullet, f.bricks):
                pygame.sprite.spritecollide(player.bullet, field_sprites, 1)
                pygame.sprite.spritecollide(player.bullet, f.bricks, 1)
                player.bullet.kill()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


def main():
    menu = Main_menu()
    cmd = menu.show()

    if cmd == 1:
        one_player_loop()


if __name__ == '__main__':
    main()
