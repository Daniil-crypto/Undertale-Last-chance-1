# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import pygame
import data

from pygame import Color, Rect
from functions import rot


class Platform():
    def __init__(self, x, y, w, h, type1, angle=0):
        self.speedx, self.speedy = 0, 0
        self.x, self.y, self.w, self.h, self.angle = x, y, w, h, angle
        self.zero_x, self.zero_y = x, y
        self.type1 = type1
        if self.type1 == "green":
            self.im = pygame.transform.scale(data.plat_green, (w, h))
        elif self.type1 == "pink":
            self.im = pygame.transform.scale(data.plat_pink, (w, h))
        self.im.set_colorkey(Color("red"))
        self.draw()

    def draw(self):
        self.x = rot(self.im, self.angle)[1][0] + self.zero_x
        self.imx, self.y = rot(self.im, self.angle)[0], rot(self.im, self.angle)[1][1] + self.zero_y
        data.pole.blit(self.imx, (self.x, self.y))
        self.rect = Rect((self.x, self.y, self.w, self.h))

    def moving(self, spx, spy):
        self.speedx = spx
        self.speedy = spy
        self.zero_x += spx
        self.zero_y += spy
        self.draw()
