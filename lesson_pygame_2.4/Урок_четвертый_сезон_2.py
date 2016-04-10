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
    '------------------------------',
    '-                            -',
    '-                            -',
    '-     ---           ---      -',
    '-                   ---      -',
    '-                            -',
    '-       ---           ---    -',
    '-                            -',
    '- --            --           -',
    '-          --                -',
    '-                            -',
    '-   ---                      -',
    '-                            -',
    '-      --                    -',
    '-                            -',
    '-             ---            -',
    '-       --                   -',
    '-   ---                      -',
    '-                            -',
    '-                            -',
    '------------------------------']

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

#Камера
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width-SIZE[0]), l)
    t = max(-(camera.height-SIZE[1]), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

total_level_width = len(level[0])*40
total_level_height = len(level)*40

camera = Camera(camera_func, total_level_width, total_level_height)

# Настройка звука
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/overworld.ogg')
sound.play(-1)

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
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))
    #sprite_group.draw(screen)

    # отображаем рабочую поверхность в окне
    window.blit(screen, (0, 0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(60)