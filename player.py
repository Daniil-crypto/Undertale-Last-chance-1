# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import math
import pygame
import data

from random import randint
from pygame import Color, Rect, Surface
from functions import change_scale, shaker


class Player():
    def __init__(self):
        global hit_s, hit1_s, blim_s, screen, sans, blim_s, GO, death
        screen, GO, sans, death = data.screen, data.GO, data.sans, data.death
        blim_s, hit1_s, hit_s = data.blim_s, data.hit1_s, data.hit_s
        self.move = False
        self.f = 1.5
        self.x, self.y, self.speed, self.w = 290, 390, 120, 16 * 2 // self.f
        self.h = 16 * 2 // self.f
        self.gravity = "down"
        self.mode = "red"
        self.speedfall = 1
        self.jumping = False
        self.start_g = 10
        self.shake_flag = False
        self.new_side = 0
        self.new_sides = []
        self.sec_d = 0
        self.all_part = []
        if self.gravity in ("down", "right"):
            self.g = -self.start_g
        elif self.gravity in ("up", "left"):
            self.g = self.start_g
        self.hp = 92
        self.krhp = 92

    def draw_player(self):
        global red_soul
        red_soul, blue_up, blue_down = data.red_soul, data.blue_up, data.blue_down
        blue_left, blue_right = data.blue_left, data.blue_right
        if self.mode == "red":
            self.pl = red_soul
        elif self.mode == "blue":
            if self.gravity == "down":
                self.pl = blue_down
            elif self.gravity == "up":
                self.pl = blue_up
            elif self.gravity == "left":
                self.pl = blue_left
            elif self.gravity == "right":
                self.pl = blue_right
        self.pl = change_scale(self.pl, self.f, self.f)
        screen.blit(self.pl, (self.x, self.y))
        self.rect = Rect(self.x, self.y, self.w, self.h)


    def movement(self, ksx=0, ksy=0, keyn="down"):
        self.move = True
        if self.mode == "red":
            self.x, self.y = self.x + self.speed * ksx // 29, self.y + self.speed * ksy // 29
        elif self.mode == "blue":
            if self.gravity in ("down", "up"):
                self.x += self.speed * ksx // 29
            elif self.gravity in ("left", "right"):
                self.y += self.speed * ksy // 29
            if keyn == self.gravity and self.collision():
                self.jumping = True
                self.phizic(0)
            if self.jumping and keyn == self.gravity:
                self.phizic(self.g)
                self.speedfall = 0
                if self.g >= 0 and (self.gravity in ("down", "right")):
                    self.jumping = False
                    self.g = -self.start_g
                    return
                if self.g <= 0 and (self.gravity in ("up", "left")):
                    self.jumping = False
                    self.g = self.start_g
                    return
                if self.gravity in ("down", "right"):
                    self.g += 0.4
                elif self.gravity in ("up", "left"):
                    self.g -= 0.4

    def phizic(self, g):
        if self.jumping:
            if self.gravity in ("down", "up"):
                self.y += g
            elif self.gravity in ("left", "right"):
                self.x += g
        elif self.collision() is False:
            if self.gravity in ("down", "left"):
                self.speedfall += g
            elif self.gravity in ("up", "right"):
                self.speedfall -= g
            if self.gravity in ("down", "up"):
                self.y += self.speedfall
            elif self.gravity in ("left", "right"):
                self.x -= self.speedfall
        else:
            self.speedfall = 0

    def collision(self, y=None):
        box, at = data.box, data.at
        f = False
        if self.y > box.y + box.h - self.w - 6 and self.gravity == "down":
            f = True
        if self.y < box.y + 6 and self.gravity == "up":
            f = True
        if self.x > box.x + box.w - self.h - 6 and self.gravity == "right":
            f = True
        if self.x < box.x + 6 and self.gravity == "left":
            f = True
        for i in at.all_platforms:
            if i.angle == 0:
                if self.gravity == "down":
                    if (self.x + self.w >= i.x + box.x and self.x <= i.x + box.x + i.w and
                        self.y + self.h >= i.y + box.y and self.y + self.h <= i.y + box.y + i.h
                        and self.jumping is False):
                        f = True
                        if i.type1 == "green":
                            self.x += i.speedx
                            self.y += i.speedy
                            i.speedx, i.speedy = 0, 0
                if self.gravity == "up":
                    if (self.x + self.w >= i.x + box.x and self.x <= i.x + box.x + i.w and
                        self.y >= i.y + box.y and self.y <= i.y + box.y + i.h
                        and self.jumping is False):
                        f = True
                        if i.type1 == "green":
                            self.x += i.speedx
                            self.y += i.speedy
                            i.speedx, i.speedy = 0, 0
                if self.gravity == "left":
                    if (self.x + self.w >= i.x + box.x + i.w - 5 and self.x <= i.x + box.x + i.w
                        and self.y + self.h >= i.y + box.y and self.y <= i.y + box.y + i.h
                        and self.jumping is False):
                        f = True
                        if i.type1 == "green":
                            self.x += i.speedx
                            self.y += i.speedy
                            i.speedx, i.speedy = 0, 0
                if self.gravity == "right":
                    if (self.x + self.w >= i.x + box.x and self.x <= i.x + box.x + 5 and
                        self.y + self.h >= i.y + box.y and self.y <= i.y + box.y + 5
                        and self.jumping is False):
                        f = True
                        if i.type1 == "green":
                            self.x += i.speedx
                            self.y += i.speedy
                            i.speedx, i.speedy = 0, 0
            elif i.angle != 0:
                if self.gravity == "down" and self.jumping == False:
                    mask1 = pygame.mask.from_surface(self.pl)
                    mask2 = pygame.mask.from_surface(i.imx)
                    if mask1.overlap_area(mask2, (int(i.x + box.x - self.x + 4),
                        int(i.y + box.y - self.y + 4))) > 0:
                        f = True
                        if i.type1 == "green":
                            self.x += i.speedx
                            self.y += i.speedy
                            i.speedx, i.speedy = 0, 0
                        elif i.type1 == "pink":
                            if 270 <= i.angle % 360 <= 360 or 0 <= i.angle % 360 <= 90:
                                self.x -= 10 * math.sin(math.radians(i.angle))
                            else:
                                self.x += 10 * math.sin(math.radians(i.angle))
                            self.y += 3 * math.sin(math.radians(i.angle))
                        self.y -= 1


        return f

    def ret_type(self):
        return self.mode

    def jum(self, knum):
        if knum == self.gravity:
            self.jumping = False
            if self.gravity in ("down", "right"):
                self.g = -self.start_g
            elif self.gravity in ("left", "up"):
                self.g = self.start_g

    def change_gravity(self, new_g, fast=True):
        self.gravity = new_g
        self.jumping = False
        if self.gravity in ("down", "right"):
            if fast:
                self.shake_flag = True
                if self.gravity == "right":
                    self.speedfall = -40
                    sans.hand_right_bool = True
                else:
                    self.speedfall = 40
                    sans.hand_down_bool = True
            else:
                self.speedfall = 0
            self.g = -self.start_g
        elif self.gravity in ("up", "left"):
            if fast:
                self.shake_flag = True
                if self.gravity == "left":
                    self.speedfall = 40
                    sans.hand_right_bool = True
                else:
                    self.speedfall = -40
                    sans.hand_up_bool = True
            else:
                self.speedfall = 0
            self.g = self.start_g
        self.new_sides.append(0)

    def check_box1(self):
        box = data.box
        if self.x < box.x + 4:
            self.x = box.x + 4
            if self.gravity == "right":
                self.jumping = False
        if self.x > box.x + box.w - 4 - self.w:
            self.x = box.x + box.w - 2 - self.w
            if self.gravity == "left":
                self.jumping = False
        if self.y < box.y + 4:
            self.y = box.y + 4
            if self.gravity == "down":
                self.jumping = False
        if self.y > box.y + box.h - 4 - self.h:
            self.y = box.y + box.h - 2 - self.h
            if self.gravity == "up":
                self.jumping = False

    def hit(self):
        global box, at
        f = False
        at, box = data.at, data.box
        sec = data.sec
        for i in at.bones:
            for j in i:
                mask1 = pygame.mask.from_surface(self.pl)
                mask2 = pygame.mask.from_surface(j.bon)
                if mask1.overlap_area(mask2, (int(j.x + box.x - self.x + 4),
                    int(j.y + box.y - self.y + 4))) > 0:
                    if j.color == "white":
                        f = True
                        if self.hp == 1:
                            self.krhp -= 1
                        self.hp -= 3
                    if j.color == "blue" and (self.move or self.speedfall != 0):
                        f = True
                        if self.hp == 1:
                            self.krhp -= 1
                        self.hp -= 3
                    if j.color == "orange" and self.move is False and self.speedfall == 0:
                        f = True
                        if self.hp == 1:
                            self.krhp -= 1
                        self.hp -= 3
        for i in at.blasters:
            if i.track1 != []:
                mask1 = pygame.mask.from_surface(self.pl)
                mask2 = pygame.mask.from_surface(i.track1)
                if mask1.overlap_area(mask2, (int(i.xxyy1[0] - self.x),
                    int(i.xxyy1[1] - self.y))) > 0:
                    f = True
                    self.hp -= 5
                    self.krhp -= 1
        if self.collision() and self.shake_flag:
            at.shaker = shaker(2, screen)
            self.shake_flag = False
            hit1_s.stop()
            hit1_s.play()

        if f:
            hit_s.stop()
            hit_s.play()

        self.hp = max(1, self.hp)
        if self.krhp <= 0 and self.hp == 1:
            self.hp = 0
        if self.hp < self.krhp:
            if sec % 3 == 0:
                self.krhp -= 1

    def change_color(self, sound=True):
        for i in range(len(self.new_sides)):
            if self.new_sides[i] == 0:
                self.new_sides[i] = 1
                if sound:
                    blim_s.play()
            if self.new_sides[i] < 25:
                player1 = change_scale(self.pl, 1 / (self.new_sides[i] * 0.1), 1 / (
                    self.new_sides[i] * 0.1)).convert_alpha()
                player1.set_colorkey((0, 0, 0))
                player1.fill((255, 0, 255, 255 - self.new_sides[i] * 10.666),
                    special_flags=pygame.BLEND_RGBA_MULT)
                x = self.x - player1.get_rect()[2] // 2 + 9
                y = self.y - player1.get_rect()[3] // 2 + 9

                screen.blit(player1, (x, y))
            self.new_sides[i] += 1

    def check_death(self):
        global sec, broken_soul, break1_s, break2_s, death, file, f1, soul_parts
        f1, soul_parts, broken_soul = data.f1, data.soul_parts, data.broken_soul
        break1_s, break2_s = data.break1_s, data.break2_s
        file = data.file
        if self.hp <= 0:
            sec = -2
            self.sec_d += 1
            if self.sec_d == 1:
                pygame.mixer.stop()
                pygame.mixer.music.stop()
                self.pl = change_scale(red_soul, self.f, self.f)
                self.alpha = 0
            if 1 <= self.sec_d:
                screen.fill(Color("black"))
                death_count = f1.render(f" - {death}", False, Color("red"))
                if self.sec_d >= 100:
                    death_count.set_alpha(755 - self.sec_d * 5)
                screen.blit(death_count, (self.x + 25, self.y))
            if self.sec_d == 120:
                pygame.mixer.music.load("music/game_over.mp3")
                pygame.mixer.music.play(-1)

            if self.sec_d > 120:
                self.alpha += 5
                self.alpha = min(self.alpha, 255)

                GO.set_alpha(self.alpha)
                screen.blit(GO, (50, 0))
            if self.sec_d < 70:
                screen.blit(self.pl, (self.x, self.y))
            if self.sec_d == 30:
                self.pl = change_scale(broken_soul, self.f, self.f)
                self.x -= 3
                break1_s.play()
            if self.sec_d == 70:
                death += 1
                file[0] = str(death)
                open("resours/data.txt", "w").write("\n".join(file))
                break2_s.play()
                for i in range(6):
                    self.all_part.append(Particle([self.x, self.y]))
            if 400 > self.sec_d > 70:
                for i in self.all_part:
                    i.move()
            return True
        return False



class Particle():
    def __init__(self, pos):
        self.step, self.sec = 0, 0
        self.im = soul_parts[0]
        self.speed_x, self.speed_y = randint(-5, 5), randint(-15, 2)
        self.g = 0.2
        self.x, self.y = pos

    def move(self):
        if self.sec % 5 == 0:
            self.step += 1
            if self.step == len(soul_parts):
                self.step = 0
            self.im = soul_parts[self.step]
        self.sec += 1
        self.speed_y += self.g
        self.x += self.speed_x
        self.y += self.speed_y
        screen.blit(self.im, (self.x, self.y))
