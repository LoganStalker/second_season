# -*- coding:utf-8 -*-

import pygame

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

# открываем игровой цикл
done = True
while done:
    # блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    # закрашиваем рабочую поверхность
    screen.fill((10, 120, 10))

    make_level(level, pl)

    # отображаем рабочую поверхность в окне
    window.blit(screen,(0, 0))
    # обновляем окно
    pygame.display.flip()