# -*- coding:utf-8 -*-

from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame.mouse import get_pos
from pygame.display import get_surface
from pygame import Surface, font

COLOR = [150, 150, 150]

font.init()

class Button(Sprite):
    def __init__(self, x=0, y=0, width=10, height=10, text='',
                 text_size=0, color=(10, 20, 130), alt_text = ''):
        Sprite.__init__(self)
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.alt_text = alt_text
        if text_size == 0:
            self.font = font.Font(None, width)
        elif text_size > 0:
            self.font = font.Font(None, text_size)
        self.color = color

    def update(self, plitki=[]):
        if len(plitki) > 1:
            for pl in plitki:
                if self != pl:
                    if collide_rect(self, pl):
                        if self.rect.x < pl.rect.x:
                            self.rect.x -= 1
                            pl.rect.x += 1
                        elif self.rect.x > pl.rect.x:
                            self.rect.x += 1
                            pl.rect.x -= 1
                        if self.rect.y < pl.rect.y:
                            self.rect.y -= 1
                            pl.rect.y += 1
                        elif self.rect.y > pl.rect.y:
                            self.rect.y += 1
                            pl.rect.y -= 1
        surf = get_surface()
        if self.rect.x <= 0:
            self.rect.x += 1
        if self.rect.y <= 0:
            self.rect.y += 1
        if self.rect.x+self.rect.w >= surf.get_width():
            self.rect.x -= 1
        if self.rect.y+self.rect.h >= surf.get_height():
            self.rect.y -= 1

        if self.mouse_on_button():
            self.image.fill((255-self.color[0], 255-self.color[1], 255-self.color[2]))
            rect(self.image, (125, 125, 125), (0, 0, self.rect.width, self.rect.height), 1)
            self.image.blit(self.font.render(self.text, 1, self.color), (3, 3))
        else:
            self.image.fill(self.color)
            rect(self.image, (255, 255, 255), (0, 0, self.rect.width, self.rect.height), 1)
            self.image.blit(self.font.render(self.text, 1, (255-self.color[0], 255-self.color[1], 255-self.color[2])), (3, 3))

    def onClick(self, mouse_click=False):
        mx, my = get_pos()
        if self.rect.x < mx and self.rect.x+self.rect.width > mx and self.rect.y < my and self.rect.y+self.rect.height > my and mouse_click:
            return 1
        else:
            return 0

    def mouse_on_button(self):
        mx, my = get_pos()
        if self.rect.x < mx and self.rect.x+self.rect.width > mx and self.rect.y < my and self.rect.y+self.rect.height > my:
            return 1
        else:
            return 0