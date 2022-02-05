# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import data
import pygame
import math

from pygame import Surface
from functions import rot, change_scale, shaker


class Atk():
    def __init__(self, col, type1, x, y, w, h, topl=False, an=90, f=1.5, shak=False, new123=False):
        global track, blast, blast_open, blaster_end_s, blaster_start_s, pole, screen, blast_open2
        global blast_open3, player
        track, blast, blast_open = data.track, data.blast, data.blast_open
        blaster_end_s, blaster_start_s = data.blaster_end_s, data.blaster_start_s
        bone_up, bone_middle, bone_down = data.bone_up, data.bone_middle, data.bone_down
        bone_up_orange, bone_middle_orange= data.bone_up_orange, data.bone_middle_orange
        bone_down_orange, bone_down_blue = data.bone_down_orange, data.bone_down_blue
        bone_up_blue, bone_middle_blue = data.bone_up_blue, data.bone_middle_blue
        pole, screen, player = data.pole, data.screen, data.player
        blast_open2, blast_open3 = data.blast_open2, data.blast_open3
        self.po1 = track.get_rect()[3] // 2
        self.x, self.y, self.h, self.w = x, y, h, w
        self.color = col
        self.type1 = type1
        self.topl = topl
        self.an = an
        self.sec = 0
        self.a = 0.5
        self.alpha = 250
        self.f = f
        self.x_y = (0, 0)
        self.x_yt = (0, 0)
        self.an1 = 0
        self.shak = shak
        self.new123 = new123
        self.track1 = []
        self.ch_s = "first"
        if type1 == "blaster":
            blaster_start_s.play()
            self.blast = change_scale(blast).convert()
            f0, f0, self.w, self.h = self.blast.get_rect()
            self.track = change_scale(track, self.f, 2.2).convert()
            self.track.set_colorkey((0, 0, 0))
        if type1 == "bone_s":
            self.bon = Surface((10, int(h)), pygame.SRCALPHA, 32)
            if self.color == "white":
                self.bon.blit(bone_up, (0, 0))
                self.bon.blit(self.change_scale(bone_middle, 1, (h - 12) / 6), (2, 6))
                self.bon.blit(bone_down, (0, h - 6))
                if self.an != 0:
                    self.bon = rot(self.bon, self.an)[0]
            if self.color == "orange":
                self.bon.blit(bone_up_orange, (0, 0))
                self.bon.blit(self.change_scale(bone_middle_orange, 1, (h - 12) / 6), (2, 6))
                self.bon.blit(bone_down_orange, (0, h - 6))
                if self.an != 0:
                    self.bon = rot(self.bon, self.an)[0]
            if self.color == "blue":
                self.bon.blit(bone_up_blue, (0, 0))
                self.bon.blit(self.change_scale(bone_middle_blue, 1, (h - 12) / 6), (2, 6))
                self.bon.blit(bone_down_blue, (0, h - 6))
                if self.an != 0:
                    self.bon = rot(self.bon, self.an)[0]
        self.draw()


    def change_scale(self, image, n1, n2):
        size = image.get_size()
        return pygame.transform.scale(image, (int(size[0] * n1), int(size[1] * n2)))


    def draw(self, sec=20, sec1=0, sec_end=30):
        self.sec += 1
        if self.type1 == "blaster":
            #Очень замудрёная система выстрелов из бластеров
            if self.sec == 1:
                if self.topl:
                    self.blast1, self.x_y = self.rotate_to_player(self.blast)[0], (
                        self.rotate_to_player(self.blast)[1][0] + self.x, self.rotate_to_player(
                        self.blast)[1][1] + self.y)
                else:
                    self.blast1, self.x_y = rot(self.blast, self.an)[0], (rot(self.blast,
                        self.an)[1][0] + self.x, rot(self.blast, self.an)[1][1] + self.y)
                    self.angle = self.an
                if self.angle == 0 or self.an == 0:
                    self.angle = 1 * 10 ** -6
                self.count = 0.18
                self.x_y = self.x_y[0] - self.pos1()[0], self.x_y[1] - self.pos1()[1] - 10
            if self.sec >= 1 and self.sec <= self.sec <= 10:
                self.x_y = (self.x_y[0] + self.pos1()[0] * self.count, self.x_y[1] +
                    self.pos1()[1] * self.count)
                self.count -= 0.018
            if self.sec == sec - 1:
                self.blast = change_scale(blast, 1.1)
                self.blast1, self.x_y = rot(self.blast, self.angle)[0], (rot(self.blast,
                    self.angle)[1][0] + self.x, rot(self.blast, self.angle)[1][1] + self.y)
            if self.sec == sec:
                blaster_start_s.stop()
                blaster_end_s.play()
                if self.shak:
                    self.spis = shaker(1, screen)
                else:
                    self.spis = []
                self.alpha = 255
                self.track.set_alpha(self.alpha)
                self.blast = change_scale(blast_open).convert()
                self.blast1, self.x_y = rot(self.blast, self.angle)[0], (rot(self.blast, self.angle
                    )[1][0] + self.x, rot(self.blast, self.angle)[1][1] + self.y)
                self.track1, self.x_yt = rot(self.track, self.angle, True, (self.w // 2, self.h
                    // 2))[0], (rot(self.track, self.angle, True, (self.w // 2, self.h // 2)
                    )[1][0], rot(self.track, self.angle, True, (self.w // 2, self.h // 2))[1][1])
            if self.sec > sec + sec1:
                B = -(self.angle - 90)
                x, y = math.cos(math.radians(B)) * 300, math.sin(math.radians(B)) * 300
                self.moving(-x / 29 * self.a, -y / 29 * self.a, True)
                self.a += 0.005 * (sec + sec1 + sec_end)
                self.alpha -= 3
                self.track.set_alpha(self.alpha)
                if sec + sec1 + 3 >= self.sec:
                    self.track = change_scale(self.track, 1.8, 2)
                elif self.track.get_size()[0] * 2 // 2.4 > 0:
                    self.track = change_scale(self.track, 2.4, 2)
                else:
                    return True
                if self.sec % 6 == 0:
                    self.blast = change_scale(blast_open2).convert()
                if self.sec % 6 == 3:
                    self.blast = change_scale(blast_open3).convert()
                self.blast1, self.x_y = rot(self.blast, self.angle)[0], (rot(self.blast,
                    self.angle)[1][0] + self.x, rot(self.blast, self.angle)[1][1] + self.y)
                self.track1, self.x_yt = rot(self.track, self.angle, True, (self.w // 2, self.h //
                    2))[0], (rot(self.track, self.angle, True, (self.w // 2, self.h // 2
                    ))[1][0], rot(self.track, self.angle, True, (self.w // 2, self.h // 2))[1][1])
                self.im = screen
                if self.spis:
                    x123, y123 = self.spis.pop(0), self.spis.pop(0)
                    screen.blit(self.im, (x123, y123))
                    screen.blit(self.track1, (self.pos()[0] + self.x + self.x_yt[0],
                        self.pos()[1] + self.y + self.x_yt[1] + 200))
            if self.sec >= sec + sec1 + sec_end:
                return True
            if self.sec >= sec:
                self.xxyy1 = (self.pos()[0] + self.x + self.x_yt[0], self.pos()[1] +
                    self.y + self.x_yt[1] + 200)
                screen.blit(self.track1, self.xxyy1)
            screen.blit(self.blast1, self.x_y)

    def moving(self, speedx, speedy, b=False):
        self.x += speedx
        self.y += speedy
        if b:
            self.x_y = speedx + self.x_y[0], speedy + self.x_y[1]

    def rotate_to_player(self, blast):
        self.angle = angle = math.degrees(math.atan2((player.x + player.w // 2) - (self.x +
            self.w // 2), (player.y + player.h // 2) - (self.y + self.h // 2)))
        image = pygame.transform.rotate(blast, angle)
        center = blast.get_rect().center
        rect = image.get_rect(center=center)
        return image, (rect[0] + 8, rect[1] + 8)

    def pos(self):
        a, b = 600, 600
        c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(self.angle))) ** 0.5
        if (2 * b * c) == 0:
            F = 0
        else: F = 90 - math.degrees(math.acos((a ** 2 - b ** 2 + c ** 2) / (2 * b * c)))
        if self.angle < 0:
            return (-math.cos(math.radians(F)) * c, -math.sin(math.radians(F)) * c)
        if 0 < self.angle < 90:
            return (math.cos(math.radians(F)) * c, -math.sin(math.radians(F)) * c)
        if 90 <= self.angle < 180:
            return (math.cos(math.radians(F)) * c, -math.sin(math.radians(F)) * c)
        return (math.cos(math.radians(F)) * c, math.sin(math.radians(F)) * c)

    def pos1(self):
        B = -(self.angle - 90)
        x, y = math.cos(math.radians(B)) * 300, math.sin(math.radians(B)) * 300
        return x * 0.9, y * 0.9
