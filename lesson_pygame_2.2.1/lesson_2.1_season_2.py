# -*- coding:utf-8 -*-

import pygame
from Player import Player

SIZE = (640, 480)

# создаем окно
window = pygame.display.set_mode(SIZE)
# создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

class Platform:
    def __init__(self):
        self.img = pygame.image.load('images/platform.png')

def make_level(level, platform):
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                screen.blit(platform.img, (x, y))
            x += 40
        y += 40
        x = 0

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

pl = Platform()

# создаем героя
hero = Player(55, 55)
left = right = False

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

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False

    # закрашиваем рабочую поверхность
    screen.fill((10, 120, 10))

    make_level(level, pl)

    # отображение героя
    hero.update(left, right)
    hero.draw(screen)

    # отображаем рабочую поверхность в окне
    window.blit(screen,(0, 0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(60)