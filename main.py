import pygame
from pyfiles.tanks.Player1Tank import Player1Tank
from pyfiles.battlefield.Field import Field
from pyfiles.MainMenu import MainMenu
from pyfiles.Game_over import Game_over

size = width, height = 800, 600
black = 0, 0, 0


def one_player_loop():
    all_sprites = pygame.sprite.Group()  # объявляем группы спрайтов

    pygame.init()
    screen = pygame.display.set_mode(size)  # инициализация pygame

    f = Field()  # инициализация поля, загрузка в field_sprites
    field_sprites = f.init_field_sprites_group() # группа спрайтов поля
    decorate = f.plants #группа декоративных спрайтов

    player = Player1Tank(all_sprites)  # инициализация танка игрока

    all_sprites.add(player)  # загрузка танка игрока

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Обновление
        all_sprites.update()
        field_sprites.update()

        screen.fill(black)

        # коллизия танка со стенами
        player.check_collisions(field_sprites)

        # отрисовка
        field_sprites.draw(screen)
        all_sprites.draw(screen)
        decorate.draw(screen)

        # коллизия снаряда с блоком
        if player.bullet_exist():
            if pygame.sprite.spritecollideany(player.bullet, f.bricks) or pygame.sprite.spritecollideany(player.bullet, f.unbreakable):
                pygame.sprite.spritecollide(player.bullet, f.bricks, 1) #уничтожить блок
                field_sprites = f.init_field_sprites_group()            #изменить поле
                player.bullet.kill()                                    #уничтожить снаряд

        # коллизия с базой
        if player.bullet_exist():
            if pygame.sprite.spritecollideany(player.bullet, f.base):
                pygame.sprite.spritecollide(player.bullet, f.base, 1)
                game_over = True                                        #завершить цикл
                game_over1 = Game_over()                                #отрисовка экрана Game Over
                game_over1.show()

        pygame.display.flip()
        pygame.time.wait(10)


def main():
    while True:
        menu = MainMenu()
        cmd = menu.show()

        if cmd == 1:
            one_player_loop()


if __name__ == '__main__':
    main()
