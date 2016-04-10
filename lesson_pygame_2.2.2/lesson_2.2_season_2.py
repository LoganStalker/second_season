# -*- coding:utf-8 -*-

import pygame
from Player import Player
from Platforms import Platform

SIZE = (640, 480)

# создаем окно
window = pygame.display.set_mode(SIZE)
# создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

# создаем героя
hero = Player(55, 55)
left = right = up = False

# создание уровня
level = [
    '----------------',
    '-              -',
    '-              -',
    '-     ---      -',
    '-              -',
    '-              -',
    '-       ---    -',
    '-              -',
    '- --           -',
    '-              -',
    '-              -',
    '----------------']

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platfroms = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platfroms.append(pl)
        x += 40
    y += 40
    x = 0

# открываем игровой цикл
done = True
timer = pygame.time.Clock()
while done:
    # блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    # закрашиваем рабочую поверхность
    screen.fill((10, 120, 10))

    # отображение героя
    hero.update(left, right, up, platfroms)
    sprite_group.draw(screen)

    # отображаем рабочую поверхность в окне
    window.blit(screen,(0, 0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(60)