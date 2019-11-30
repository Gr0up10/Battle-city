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
    player_group.add(player)  # загрузка танка игрока

    enemy1 = Enemy(bullets_group, bullets, 40, 40)  # инициализация врагов
    tanks_sprites.add(enemy1)
    enemy2 = Enemy(bullets_group, bullets, 80, 40)  # инициализация врагов
    tanks_sprites.add(enemy2)
    enemy2.kill()
    enemy3 = Enemy(bullets_group, bullets, 120, 40)  # инициализация врагов
    tanks_sprites.add(enemy3)
    enemy3.kill()
    enemy4 = Enemy(bullets_group, bullets, 160, 40)  # инициализация врагов
    tanks_sprites.add(enemy4)
    enemy4.kill()
    enemy_list = [enemy1,enemy2,enemy3,enemy4]
    ticks = 0

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if ticks >= 5000:
            for enemy in enemy_list:
                if not enemy.isAlive:
                    #print(enemy_list[enemy])
                    enemy = Enemy(bullets_group,bullets,40,40)
                    tanks_sprites.add(enemy)
                    ticks = 0
                    break
                else:
                    ticks = 0
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
            enemy.check_collisions(player_field)


        # отрисовка
        field_sprites.draw(screen)
        tanks_sprites.draw(screen)
        bullets_group.draw(screen)
        decorate.draw(screen)
        player_group.draw(screen)

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
                    game_over = True                # завершить цикл
                    game_over1 = Game_over()        # отрисовка экрана Game Over
                    game_over1.show()

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
