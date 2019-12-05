import pygame
from pyfiles.tanks.Player1 import Player1
from pyfiles.battlefield.Field import Field
from pyfiles.menu.Game_over import Game_over
from pyfiles.tanks.Enemy import Enemy
from pyfiles.tanks.Player2 import Player2

size = width, height = 800, 600
black = 0, 0, 0
white = 255, 255, 255


def game_over_screen(label):
    screen = Game_over(label)
    screen.show()
    return True


def merge_sprites_group(tanks, field):
    all_sprites = pygame.sprite.Group()
    for b in tanks:
        all_sprites.add(b)
    for b in field:
        all_sprites.add(b)
    return all_sprites


class GameLoop:
    def __init__(self):
        pass

    def one_player_loop(self, level_num, two= False):
        tanks_sprites = pygame.sprite.Group()  # объявляем группы спрайтов
        player1_group = pygame.sprite.Group()
        bullets_group = pygame.sprite.Group()
        bullets_of_player1 = pygame.sprite.Group()
        bullets_of_enemies = pygame.sprite.Group()

        bullets = list()

        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 50, True)
        enemies_count = '10'
        player_lifes_count = '30'

        pygame.init()
        screen = pygame.display.set_mode(size)  # инициализация pygame

        f = Field(level_num)  # инициализация поля, загрузка в field_sprites
        print(level_num)
        field_sprites = f.init_field_sprites_group()  # группа спрайтов поля
        decorate = f.plants  # группа декоративных спрайтов

        tank_player = Player1(bullets_of_player1, bullets)  # инициализация танка игрока
        player1_group.add(tank_player)  # загрузка танка игрока

        if two:
            player2 = Player2(bullets_of_player1, bullets)
            player1_group.add(player2)

        pygame.font.init() # Инициализация текста
        enemy1 = Enemy(bullets_of_enemies, bullets, 40, 40, player1_group, '1')  # инициализация врагов

        tanks_sprites.add(enemy1)
        enemy_list = list()
        enemy_list.append(enemy1)

        ticks = 0
        enemies_count_flag = True

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            for enemy in enemy_list:
                if not enemy.alive():
                    enemy_list.remove(enemy)

            if ticks >= 300:
                if len(enemy_list) < 4 and int(enemies_count) > 0:
                    new_enemy = Enemy(bullets_of_enemies, bullets, 40, 40, player1_group, '2')
                    enemy_list.append(new_enemy)
                    tanks_sprites.add(new_enemy)
                    ticks = 0
                else:
                    ticks = 300
            # Обновление
            tanks_sprites.update()
            field_sprites.update()
            player1_group.update()
            bullets_group.update()
            bullets_of_player1.update()
            bullets_of_enemies.update()

            screen.fill(black)

            # подготовка к отработке коллизий
            tanks_field = merge_sprites_group(tanks_sprites, field_sprites)
            player_field = merge_sprites_group(player1_group, field_sprites)
            # коллизия танка
            for player in player1_group:
                temp = merge_sprites_group(tanks_field, player1_group)
                temp.remove(player)
                player.check_collisions(temp)
            for enemy in enemy_list:
                if enemy.alive():
                    temp = merge_sprites_group(tanks_field, player_field)
                    temp.remove(enemy)
                    enemy.check_collisions(temp)

            # отрисовка
            field_sprites.draw(screen)
            tanks_sprites.draw(screen)
            bullets_group.draw(screen)
            bullets_of_player1.draw(screen)
            bullets_of_enemies.draw(screen)
            player1_group.draw(screen)
            decorate.draw(screen)
            ts = font.render(enemies_count, False, white)
            ts2 = font.render(player_lifes_count, False, white)
            screen.blit(ts, (700, 500))
            screen.blit(ts2, (700, 400))

            # коллизия снарядов с полем
            if len(bullets) > 0:
                for b in bullets:  # удалить "мёртвые" снаряды (оптимизация)
                    if not b.alive():
                        bullets.remove(b)

                for b in bullets:  # коллизия снарядов и блоков
                    if pygame.sprite.spritecollideany(b, f.bricks) or pygame.sprite.spritecollideany(b, f.unbreakable):
                        collided = pygame.sprite.spritecollide(b, f.bricks, True)  # уничтожить блок
                        # for i in collided:                         # это старый функционал разрушаемости блоков.
                        # i.take_damage(b.direction)
                        field_sprites = f.init_field_sprites_group()  # изменить поле
                        b.kill()

                for b in bullets:  # коллизия снарядов и базы
                    if pygame.sprite.spritecollideany(b, f.base):
                        pygame.sprite.spritecollide(b, f.base, 1)
                        game_over = game_over_screen('Game over')
                        return 'lose'

                for b in bullets:  # коллизия снарядов и танка игрока
                    if pygame.sprite.spritecollideany(b, player1_group):
                        collided = pygame.sprite.spritecollide(b, player1_group, False)
                        player_lifes_count = str(int(player_lifes_count) - 1)
                        if int(player_lifes_count) <= 0:
                            game_over = game_over_screen('Game over')
                            return 'lose'
                        else:
                            print('===', len(player1_group))
                            for i in collided:
                                i.respawn()
                            for tank in tanks_sprites:
                                tank.player = player1_group

                for b in bullets:  # коллизия снаряда и противника
                    if pygame.sprite.spritecollide(b, tanks_sprites, True):
                        if enemies_count_flag:
                            enemies_count = str(int(enemies_count) - 1)
                        if (int(enemies_count)) == 0:
                            enemies_count_flag = False
                            game_over = game_over_screen('You won!')
                            return 'win'
                        b.kill()
                        for enemy in enemy_list:
                            if not enemy.isAlive:
                                enemy = Enemy(bullets_of_enemies, bullets, 40, 40, player1_group, '2')
                                tanks_sprites.add(enemy)

                pygame.sprite.groupcollide(bullets_of_enemies, bullets_of_player1, True, True)  # коллизия снарядов

            pygame.display.flip()
            pygame.time.wait(10)
            ticks += 1
