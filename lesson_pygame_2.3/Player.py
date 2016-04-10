# -*- coding:utf-8 -*-

from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pyganim

MOVE_SPEED = 7
JUMP_POWER = 10

GRAVITY = 0.4
COLOR = (10, 120, 10)

ANIMATION_DELAY = 0.1
ANIMATION_STAY = [('images/hero/hero.png', ANIMATION_DELAY)]

ANIMATION_RIGHT = ['images/hero/hero_right1.png',
                   'images/hero/hero_right2.png',
                   'images/hero/hero_right3.png']
ANIMATION_LEFT = ['images/hero/hero_left1.png',
                   'images/hero/hero_left2.png',
                   'images/hero/hero_left3.png']
ANIMATION_UP = ['images/hero/hero_up1.png',
                   'images/hero/hero_up2.png',
                   'images/hero/hero_up3.png',
                   'images/hero/hero_up4.png']

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimUp = make_boltAnim(ANIMATION_UP, ANIMATION_DELAY)
        self.boltAnimUp.play()

    def update(self, left, right, up, platforms):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimRight.blit(self.image, (0, 0))
        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill(COLOR)
                self.boltAnimStay.blit(self.image, (0, 0))

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(COLOR)
            self.boltAnimUp.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0
