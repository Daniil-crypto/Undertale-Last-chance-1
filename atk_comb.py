# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import pygame
import data

from atk import Atk
from pygame import Surface, Color

class Atk_comb():
    def __init__(self):
        global pole, player, box, at, pole1
        player, box, pole, pole1, at = data.player, data.box, data.pole, data.pole1, data.at
        self.sec = 0
        self.bone = []
        self.ya = True

    def bone_strike(self, height, side, sec, sec2, sec3, push=True):
        self.sec += 1
        if self.sec == 1:
            if side in ("down", "up"):
                self.atk = Surface((box.w, height))
            if side in ("left", "right"):
                self.atk = Surface((height, box.h))
            if push:
                player.change_gravity(side, True)
        if sec <= self.sec < sec + sec2:
            if side in ("down", "up"):
                if self.sec % 6 == 0:
                    pygame.draw.rect(self.atk, Color("red"), (1, 0, box.w, height - 4), 2)
                elif self.sec % 6 == 3:
                    pygame.draw.rect(self.atk, Color("yellow"), (1, 0, box.w - 7, height - 4), 2)
            if side in ("left",  "right"):
                if self.sec % 6 == 0:
                    pygame.draw.rect(self.atk, Color("red"), (0, 1, height - 4, box.h - 7), 2)
                elif self.sec % 6 == 3:
                    pygame.draw.rect(self.atk, Color("yellow"), (0, 1, height - 4, box.h - 7), 2)
        if self.sec == sec + sec2:
            if side == "down":
                for i in range(box.w // 10):
                    self.bone.append(Atk("white", "bone_s", i * 12, box.h, 10, height, False, 0))
            if side == "up":
                for i in range(box.w // 10):
                    self.bone.append(Atk("white", "bone_s", i * 12, 0 - height, 10, height,
                        False, 180))
            if side == "left":
                for i in range(box.h // 10):
                    self.bone.append(Atk("white", "bone_s", 0 - height, i * 12, 10, height,
                        False, 270))
            if side == "right":
                for i in range(box.h // 10):
                    self.bone.append(Atk("white", "bone_s", box.w, i * 12, 10, height, False, 90))
            at.bones.append(self.bone)
        if self.sec > sec + sec2 and self.sec <= sec + sec2 + 5:
            self.ya = False
            if side == "down":
                for i in self.bone:
                    i.moving(0, -(height / 5 - 0.5))
            if side == "up":
                for i in self.bone:
                    i.moving(0, (height / 5 - 1.5))
            if side == "left":
                for i in self.bone:
                    i.moving((height / 5 - 1.5), 0)
            if side == "right":
                for i in self.bone:
                    i.moving(-(height / 5 - 0.5), 0)
        if self.sec > sec + sec2 + sec3 - 5 and self.sec <= sec + sec2 + sec3:
            self.ya = False
            if side == "down":
                for i in self.bone:
                    i.moving(0, (height / 5 - 0.5))
            if side == "up":
                for i in self.bone:
                    i.moving(0, -(height / 5 - 1.5))
            if side == "left":
                for i in self.bone:
                    i.moving(-(height / 5 - 1.5), 0)
            if side == "right":
                for i in self.bone:
                    i.moving((height / 5 - 0.5), 0)

        if self.ya:
            if side == "up":
                data.pole.blit(self.atk, (0, 1))
            if side == "down":
                data.pole.blit(self.atk, (0, box.h - height - 2))
            if side == "left":
                data.pole.blit(self.atk, (1, 1))
            if side == "right":
                data.pole.blit(self.atk, (box.w - height - 2, 0))
