# -*- coding:utf-8 -*-

from pygame.sprite import Sprite
from pygame import Surface

MOVE_SPEED = 7
GRAVITY = 0.4

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((22, 32))
        self.image.fill((150, 150, 150))
        self.xvel = 0
        self.yvel = 0
        self.x = x
        self.y = y
        self.onGroung = False

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if not(left or right):
            self.xvel = 0

        if not self.onGroung:
            self.yvel += GRAVITY

        self.x += self.xvel
        self.y += self.yvel

    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))