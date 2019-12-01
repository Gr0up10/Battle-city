import pygame
from pyfiles.tanks.Player1Tank import Player1Tank
from pyfiles.battlefield.Field import Field
from pyfiles.MainMenu import MainMenu
from pyfiles.Game_over import Game_over
from pyfiles.tanks.Enemy import Enemy

size = width, height = 800, 600
black = 0, 0, 0
white = 255, 255, 255


def game_over_screen():
    screen = Game_over()
    screen.show()
    return True


def merge_sprites_group(tanks, field):
    all_sprites = pygame.sprite.Group()
    for b in tanks:
        all_sprites.add(b)
    for b in field:
        all_sprites.add(b)
    return all_sprites


def one_player_loop():
    tanks_sprites = pygame.sprite.Group()  # объявляем группы спрайтов
    player_group = pygame.sprite.GroupSingle()
    bullets_group = pygame.sprite.Group()
    bullets = list()

    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50, True)
    data = '20'


    pygame.init()
    screen = pygame.display.set_mode(size)  # инициализация pygame

    f = Field()  # инициализация поля, загрузка в field_sprites
    field_sprites = f.init_field_sprites_group() # группа спрайтов поля
    decorate = f.plants # группа декоративных спрайтов

    player = Player1Tank(bullets_group, bullets)  # инициализация танка игрока
    player_group.add(player)  # загрузка танка игрока
    pygame.font.init() # Инициализация текста
    enemy1 = Enemy(bullets_group, bullets, 40, 40)  # инициализация врагов
    tanks_sprites.add(enemy1)
    enemy_list = list()
    enemy_list.append(enemy1)

    ticks = 0
    data_flag = True
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        for enemy in enemy_list:
            if not enemy.alive():
                enemy_list.remove(enemy)

        if ticks >= 300:
            if len(enemy_list) < 4 and int(data) > 0:
                new_enemy = Enemy(bullets_group, bullets, 40, 40)
                enemy_list.append(new_enemy)
                tanks_sprites.add(new_enemy)
                ticks = 0
            else:
                ticks = 300


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
        for enemy in enemy_list:
            if enemy.alive():
                enemy.check_collisions(player_field)


        # отрисовка
        field_sprites.draw(screen)
        tanks_sprites.draw(screen)
        bullets_group.draw(screen)
        decorate.draw(screen)
        player_group.draw(screen)
        ts = font.render(data, False, white)
        screen.blit(ts, (700, 500))

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

            for b in bullets:           # коллизия снаряда и противника
                if pygame.sprite.spritecollide(b, tanks_sprites, True):
                    print('enemy destroyed')
                    if data_flag:
                        data = str(int(data) - 1)
                    if (int(data)) == 0:
                        data_flag = False
                    b.kill()
                    for enemy in enemy_list:
                        if not enemy.isAlive:
                            enemy = Enemy(bullets_group, bullets, 40, 40)
                            tanks_sprites.add(enemy)

        pygame.display.flip()
        pygame.time.wait(10)
        ticks+=1


def main():
    while True:
        menu = MainMenu()
        cmd = menu.show()

        if cmd == 1:
            one_player_loop()


if __name__ == '__main__':
    main()
