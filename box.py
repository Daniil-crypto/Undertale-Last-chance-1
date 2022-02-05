# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import pygame
import data

from pygame import Color, Surface


class Box():
    def __init__(self, x, y, w, h):
        global pole, pole1, screen
        self.x, self.y, self.w, self.h = x, y, w, h
        screen = data.screen
        data.pole1 = pole1 = Surface((self.w + 4, self.h + 4))
        data.pole = pole = Surface((self.w - 4, self.h - 4))
        self.change()
        self.start()

    def start(self):
        self.change()
        pole1.fill(Color("black"))
        self.draw()

    def change_size(self, spw, sph):
        self.x += spw
        self.y += sph
        self.w -= spw * 2
        self.h -= sph * 2
        self.draw()

    def draw(self):
        pygame.draw.rect(pole1, Color("white"), (2, 2, self.w, self.h), 5)

    def surf(self):
        screen.blit(pole1, (self.x, self.y))
        screen.blit(pole, (self.x + 4, self.y + 4))
        self.draw()

    def change_pos(self, spw, sph):
        self.x += spw
        self.y += sph
        self.draw()

    def change(self):
        global pole1, pole
        data.pole1 = pole1 = Surface((self.w + 4, self.h + 4))
        data.pole = pole = Surface((self.w - 4, self.h - 4))
