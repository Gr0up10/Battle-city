import pygame
from pyfiles.tanks.Player1Tank import Player1Tank
from pyfiles.battlefield.Field import Field
from pyfiles.MainMenu import MainMenu
from pyfiles.Game_over import Game_over
from pyfiles.tanks.Enemy import Enemy

size = width, height = 800, 600
black = 0, 0, 0


def merge_sprites_group(tanks, field):
    all_sprites = pygame.sprite.Group()
    for b in tanks:
        all_sprites.add(b)
    for b in field:
        all_sprites.add(b)
    return all_sprites


def game_over_screen():
    game_over1 = Game_over()  # отрисовка экрана Game Over
    game_over1.show()
    return True


def one_player_loop():
    tanks_sprites = pygame.sprite.Group()  # объявляем группы спрайтов
    player_group = pygame.sprite.GroupSingle()
    bullets_group = pygame.sprite.Group()
    bullets = list()

    pygame.init()
    screen = pygame.display.set_mode(size)  # инициализация pygame

    f = Field()  # инициализация поля, загрузка в field_sprites
    field_sprites = f.init_field_sprites_group() # группа спрайтов поля
    decorate = f.plants # группа декоративных спрайтов

    player = Player1Tank(bullets_group, bullets)  # инициализация танка игрока
    enemy = Enemy(bullets_group, bullets)

    player_group.add(player)  # загрузка танка игрока
    tanks_sprites.add(enemy)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Обновление
        tanks_sprites.update()
        field_sprites.update()
        player_group.update()
        bullets_group.update()

        screen.fill(black)

        # подготовка к отработке коллизий
        tanks_field = merge_sprites_group(tanks_sprites, field_sprites)
        player_field = merge_sprites_group(player_group, field_sprites)
        # коллизия танка
        player.check_collisions(tanks_field)
        enemy.check_collisions(player_field)

        # отрисовка
        field_sprites.draw(screen)
        tanks_sprites.draw(screen)
        bullets_group.draw(screen)
        player_group.draw(screen)
        decorate.draw(screen)

        # коллизия снарядов с полем
        if len(bullets) > 0:
            for b in bullets:             # удалить "мёртвые" снаряды (оптимизация)
                if not b.alive():
                    bullets.remove(b)

            for b in bullets:           # коллизия снарядов и блоков
                if pygame.sprite.spritecollideany(b, f.bricks) or pygame.sprite.spritecollideany(b, f.unbreakable):
                    pygame.sprite.spritecollide(b, f.bricks, 1)  # уничтожить блок
                    field_sprites = f.init_field_sprites_group()  # изменить поле
                    b.kill()

            for b in bullets:           # коллизия снарядов и базы
                if pygame.sprite.spritecollideany(b, f.base):
                    pygame.sprite.spritecollide(b, f.base, 1)
                    game_over = game_over_screen()
                    print('Base destroyed')

            for b in bullets:           # коллизия снарядов и танка игрока
                if pygame.sprite.spritecollide(b, player_group, True):
                    game_over = game_over_screen()
                    print(b.rect.x, b.rect.y)
                    print(player.rect.x, player.rect.y)
                    print('tank destroyed')

            for b in bullets:
                if pygame.sprite.spritecollide(b, tanks_sprites, True):
                    print('enemy destroyed')
                    tanks_sprites.remove(enemy)
                    b.kill()
                    enemy = Enemy(bullets_group, bullets)
                    tanks_sprites.add(enemy)

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
