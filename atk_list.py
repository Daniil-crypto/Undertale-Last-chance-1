# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import pygame
import data

from atk import Atk
from pygame import Color
from atk_comb import Atk_comb
from platform_x import Platform
from random import randint


class AtkList():
    def __init__(self):
        global screen, bam, sec
        screen, screen1 = data.screen, data.screen1
        sec = 0
        bam = data.bam
        self.clear()

    def all_atks(self):
        global diologs, player, box, legs, face_ser, face, hand_down, hand_up, hand_right
        global sans, pole, tors_1, tors_2, sec, sec1
        sec1 = round(pygame.mixer.music.get_pos() / 1000 * 29)
        if sec1 == sec:
            sec = sec1 + 1
        elif sec1 == sec + 2:
            sec = sec1 - 1
        else:
            sec = sec1
        if self.skip:
            sec += 1010
        self.c_h_bool = False
        all_txts = data.all_txts
        if sec == -1:
            return
        if sec == 0:
            data.screen.set_alpha(0)
            pole, pole1 = data.pole, data.pole1
            diologs, player, box = data.diologs, data.player, data.box
            legs, face_ser, face, hand_down = data.legs, data.face_ser, data.face, data.hand_down
            hand_up, hand_right = data.hand_up, data.hand_right
            tors_1, tors_2 = data.tors_1, data.tors_2
            sans = data.sans

        if 0 < sec < 255:
            screen.set_alpha(sec)

        if sec == 430:
            sans.face = face_ser
            self.change = True
            bam.play()
        if sec == 445:
            self.change = False
            bam.play()
        if 240 <= sec < 420:
            if sec % 60 == 20:
                player.new_sides.append(0)
                player.change_color(False)
        if sec == 230:
            diologs.txt, diologs.time, diologs.txt1 = all_txts[41], 0, ""
        if 230 <= sec < 295:
            diologs.draw_all(340, 150)
        if sec == 295:
            diologs.txt, diologs.time, diologs.txt1, diologs.txt2 = all_txts[42], 0, "", ""
            diologs.next, diologs.stop = False, False
        if 295 <= sec < 370:
            diologs.draw_all(340, 150)
        if sec == 380:
            diologs.txt, diologs.time, diologs.txt1, diologs.txt2 = all_txts[43], 0, "", ""
            diologs.next, diologs.stop = False, False
        if 370 <= sec < 430:
            diologs.draw_all(340, 150)
        if sec == 445:
            diologs.txt, diologs.time, diologs.txt1, diologs.txt2 = all_txts[44], 0, "", ""
            diologs.next, diologs.stop = False, False
        if 445 <= sec < 498:
            diologs.draw_all(340, 150, False)
        if 455 <= sec < 480:
            self.c_h = (sec - 455) * 40
            self.c_h_bool = True
            self.c_x, self.c_y = -(sec - 455) * 40 / 2, -(sec - 455) * 40 / 2 + (sec - 455) * 10
        if sec == 500:
            sans.mov = True
        if 480 <= sec <= 505:
            self.c_h = -(sec - 505) * 40
            self.c_h_bool = True
            self.c_x, self.c_y = (sec - 505) * 40 / 2, (sec - 505) * 40 / 2 + -(sec - 505) * 10
        if 500 <= sec <= 1000:
            self.block1()
        if sec == 1015:
            sans.face = face_ser
            sans.tors = tors_2
            sans.x_t -= 18
            sans.y_t += 2
        if sec == 1055:
            bam.play()
            player.x, player.y = 290, 390
            player.blok, player.mode, player.gravity = False, "blue", "down"
            sans.face = face[0]
            sans.tors = tors_1
            sans.x_t += 18
            sans.y_t -= 2
            sans.x, sans.y = 100, 100
            box.x, box.y, box.w, box.h = 140, 260, 400, 240 #200, 300, 200, 200
            self.clear()
            self.change = True
        if sec == 1075:
            player.blok = True
            bam.play()
            self.change = False
        if 1075 <= sec <= 1875:
            self.block2()
        if sec == 1875:
            self.change = True
            player.blok = False
            bam.play()

            ## ВРЕМЕННО ##
            pygame.mixer.music.set_volume(0)
        if sec == 1900:
            self.change = False
            data.intro.play()
            data.end = True



    def block1x(self):
        self.b1_sec += 1
        if self.b1_sec == 1:
            self.blok = True
            player.mode = "blue"
            self.atk1()
        if self.b1_sec >= 1 and self.b1_sec < 150:
            self.bone_str[0].bone_strike(120, "down", 10, 32, 80, False)
        if self.b1_sec == 60:
            self.atk1()
        if self.b1_sec >= 60 and self.b1_sec < 150:
            self.bone_str[1].bone_strike(120, "left", 10, 8, 44, True)
        if self.b1_sec == 100:
            player.mode = "red"
            self.blasters.append(Atk("white", "blaster", 320, 200, 60, 60, False, 360))
            self.blasters.append(Atk("white", "blaster", 420, 280, 60, 60, False, -90))
        if self.b1_sec == 104:
            self.blasters.append(Atk("white", "blaster", 300, 200, 60, 60, False, 360))
            self.blasters.append(Atk("white", "blaster", 420, 300, 60, 60, False, -90))
        if self.b1_sec == 108:
            self.blasters.append(Atk("white", "blaster", 280, 200, 60, 60, False, 360))
            self.blasters.append(Atk("white", "blaster", 420, 320, 60, 60, False, -90))
        if self.b1_sec == 112:
            self.blasters.append(Atk("white", "blaster", 260, 200, 60, 60, False, 360))
            self.blasters.append(Atk("white", "blaster", 420, 340, 60, 60, False, -90))
        if self.b1_sec == 116:
            self.blasters.append(Atk("white", "blaster", 240, 200, 60, 60, False, 360))
            self.blasters.append(Atk("white", "blaster", 420, 360, 60, 60, False, -90))
        if self.b1_sec == 150:
            player.gravity = "down"
            player.mode = "blue"
            self.bones = []
            self.bone_str = []
        if self.b1_sec == 155:
            self.blasters.append(Atk("white", "blaster", 200, 200, 60, 60, False, 360, 1.5, True))
            self.blasters.append(Atk("white", "blaster", 320, 200, 60, 60, False, 360, 1.5, True))
            self.blasters.append(Atk("white", "blaster", 420, 280, 60, 60, False, -90))
            self.blasters.append(Atk("white", "blaster", 420, 400, 60, 60, False, -90))
            self.blasters.append(Atk("white", "blaster", 100, 280, 60, 60, False, 90))
            self.blasters.append(Atk("white", "blaster", 100, 400, 60, 60, False, 90))
        if self.b1_sec == 165:
            player.change_gravity("up", True)
        if 190 <= self.b1_sec <= 195:
            box.change_size(-15, 0)
            box.change_pos(8, 0)
        if self.b1_sec == 200:
            player.change_gravity("right", False)
            for i in range(250):
                self.bones1.append(Atk("white", "bone_s", 260, 250 + i * 15, 10, 120, False, 90))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(50):
                if i < 6:
                    self.bones1.append(Atk("white", "bone_s", -100 - 32 * i, 180 - i * 20,
                        10, 20 + i * 20, False, 0))
                    self.bones1.append(Atk("white", "bone_s", -100 - 32 * i, 0, 10,
                        120 - i * 20, False, 0))
                if 11 > i >= 6:
                    j = 11 - i
                    self.bones1.append(Atk("white", "bone_s", -100 - 32 * i, 180 - j * 20,
                        10, 20 + j * 20, False, 0))
                    self.bones1.append(Atk("white", "bone_s", -100 - 32 * i, 0, 10,
                        120 - j * 20, False, 0))
                if 16 > i >= 11:
                    j = i - 10
                    self.bones1.append(Atk("white", "bone_s", -140 - 32 * i,
                        180 - j * 20, 10, 20 + j * 20, False, 0))
                    self.bones1.append(Atk("white", "bone_s", -140 - 32 * i, 0, 10,
                        120 - j * 20, False, 0))
                if 21 > i >= 16:
                    j = 21 - i
                    self.bones1.append(Atk("white", "bone_s", -140 - 32 * i, 180 - j * 20,
                        10, 20 + j * 20, False, 0))
                    self.bones1.append(Atk("white", "bone_s", -140 - 32 * i, 0, 10,
                        120 - j * 20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
        if 580 > self.b1_sec > 200:
            for i in self.bones:
                for j in i:
                    if self.bones.index(i) == 0:
                        j.moving(0, -3)
                    if self.bones.index(i) == 1:
                        j.moving(3, 0)
        if self.b1_sec == 270:
            player.change_gravity("down", True)
        if 535 >= self.b1_sec >= 530:
            box.change_size(15, 0)
            box.change_pos(-8, 0)
        if 545 >= self.b1_sec >= 540:
            box.change_size(0, -15)
            box.change_pos(0, -8)
        if self.b1_sec == 550:
            self.bones = []
            player.change_gravity("up", True)
        if 800 >= self.b1_sec >= 580:
            if self.b1_sec % 20 == 0:
                self.blasters.append(Atk("white", "blaster", 195, 60, 60, 60, False, 360))
                self.blasters.append(Atk("white", "blaster", 330, 60, 60, 60, False, 360))
        if self.b1_sec == 580:
            for i in range(70):
                self.bones1.append(Atk("white", "bone_s", -50 - 15 * i, 50, 10, 400, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(50):
                if i < 4:
                    self.bones1.append(Atk("white", "bone_s", 140 - i * 10, -100 - 20 * i,
                        10, 100 + i * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - i * 10,
                        False, 90))
                if 4 <= i < 8:
                    j = 8 - i
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
                if 8 <= i < 12:
                    j = i - 8
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
                if 12 <= i < 16:
                    j = 16 - i
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
                if 16 <= i < 20:
                    j = i - 16
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
                if 20 <= i < 24:
                    j = 24 - i
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
                if 24 <= i < 28:
                    j = i - 24
                    self.bones1.append(Atk("white", "bone_s", 140 - j * 10, -100 - 20 * i, 10,
                        100 + j * 10, False, 90))
                    self.bones1.append(Atk("white", "bone_s", 0, -100 - 20 * i, 10, 100 - j *
                        10, False, 90))
            self.bones.append(self.bones1)
            self.bones1 = []
        if 850 >= self.b1_sec >= 580:
            for i in self.bones:
                for j in i:
                    if self.bones.index(i) == 0:
                        j.moving(5, 0)
                    if self.bones.index(i) == 1:
                        j.moving(0, 5)
        if self.b1_sec == 850:
            self.bones = []
            player.mode = "red"
        if 850 <= self.b1_sec <= 855:
            box.change_size(0, 15)
            box.change_pos(0, 8)
        if 853 <= self.b1_sec <= 856:
            box.change_size(-25, 0)
        if 860 <= self.b1_sec <= 1000:
            self.atk2(self.b1_sec)
        if self.b1_sec == 1010:
            for i in range(4):
                self.blasters.append(Atk("white", "blaster", 100 + 105 * i, 200, 60, 60,
                    False, 360))
        if self.b1_sec == 1034:
            for i in range(3):
                self.blasters.append(Atk("white", "blaster", 152 + 105 * i, 200, 60, 60,
                    False, 360))
        if self.b1_sec == 1058:
            for i in range(4):
                self.blasters.append(Atk("white", "blaster", 100 + 105 * i, 200, 60, 60,
                    False, 360))

    def block1(self):
        self.b2_sec += 1
        if self.b2_sec == 1:
            player.mode = "blue"
            self.blok = True
            self.bone_str.append(Atk_comb())
        if self.b2_sec >= 1 and self.b1_sec <= 30:
            self.bone_str[0].bone_strike(80, "down", 1, 7, 15)
        if self.b2_sec == 20:
            for i in range(8):
                self.bones1.append(Atk("white", "bone_s", 5 + box.w + i * 25, 0, 10,
                    71 - i * 8, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(8):
                self.bones1.append(Atk("white", "bone_s", -5 - i * 25, 125 + i * 8, 10,
                    71 - i * 8, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
        if self.b2_sec == 23:
            player.change_gravity("down", True)
        if 20 <= self.b2_sec <= 72:
            for i in self.bones:
                for j in i:
                    if self.bones.index(i) == 1:
                        j.moving(-10, 0)
                    if self.bones.index(i) == 2:
                        j.moving(10, 0)
        if self.b2_sec == 40:
            player.change_gravity("up", True)
            self.blasters.append(Atk("white", "blaster", 100, 270, 60, 60, False, 90))
        if self.b2_sec == 44:
            player.change_gravity("right", True)
        if 48 >= self.b2_sec >= 42:
            sans.x -= 30
            box.change_pos(8, 0)
            box.change_size(-10, 0)
        if self.b2_sec == 59:
            player.change_gravity("down", True)
        if self.b2_sec == 60:
            for i in range(3):
                self.bones1.append(Atk("white", "bone_s", 5 - i * 25, 0, 10, 50 - i * 8,
                    False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(3):
                self.bones1.append(Atk("white", "bone_s", 5 - i * 25, 150 + i * 8, 10,
                    50 - i * 8, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            self.all_platforms.append(Platform(-280, 120, 80, 11, "green", 0))
            for i in range(10):
                self.bones1.append(Atk("white", "bone_s", -180 - i * 25, 0, 10, 20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(25):
                self.bones1.append(Atk("white", "bone_s", -180 - i * 25, 170, 10, 20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(85):
                self.bones1.append(Atk("white", "bone_s", -180 - 25 * 25 - i * 25, 0, 10,
                    20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(11):
                if i % 2 == 1:
                    self.bones1.append(Atk("white", "bone_s", -180 - 25 * 25 - i * 150 - 200,
                        170, 10, 20, False, 0))
                else:
                    self.bones1.append(Atk("blue", "bone_s", -180 - 25 * 25 - i * 150 - 200,
                        40, 10, 160, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
        if 60 <= self.b2_sec <= 329:
            for i in self.bones:
                self.ind_j = 0
                for j in i:
                    if self.bones.index(i) in range(2, 10):
                        j.moving(self.speed_b2, 0)
                    if (self.bones.index(i) == 3 and self.b2_sec < 100 and
                        self.bones[3][self.bones[3].index(j)].ch_s == "first"):
                        self.ind_j = self.bones[3].index(j)
                        self.bones[3][self.ind_j] = Atk("white", "bone_s",
                            self.bones[3][self.bones[3].index(j)].x,
                            self.bones[3][self.bones[3].index(j)].y,
                            self.bones[3][self.bones[3].index(j)].w,
                            self.bones[3][self.bones[3].index(j)].h + 2.5, False, 0)
                    elif (self.bones.index(i) == 3 and self.b2_sec < 100 and
                        self.bones[3][self.bones[3].index(j)].ch_s == "second"):
                        self.ind_j = self.bones[3].index(j)
                        if self.bones[3][self.ind_j].h > 15:
                            self.bones[3][self.ind_j] = Atk("white", "bone_s",
                                self.bones[3][self.bones[3].index(j)].x,
                                self.bones[3][self.bones[3].index(j)].y,
                                self.bones[3][self.bones[3].index(j)].w,
                                self.bones[3][self.bones[3].index(j)].h - 2.5, False, 0)
                            self.bones[3][self.ind_j].ch_s = "second"
                    if (self.bones.index(i) == 4 and self.b2_sec < 100 and
                        self.bones[4][self.bones[4].index(j)].ch_s == "first"):
                        self.ind_j = self.bones[4].index(j)
                        self.bones[4][self.ind_j] = Atk("white", "bone_s",
                            self.bones[4][self.bones[4].index(j)].x,
                            self.bones[4][self.bones[4].index(j)].y - 2.5,
                            self.bones[4][self.bones[4].index(j)].w,
                            self.bones[4][self.bones[4].index(j)].h + 2.5, False, 0)
                    elif (self.bones.index(i) == 4 and self.b2_sec < 100 and
                        self.bones[4][self.bones[4].index(j)].ch_s == "second"):
                        self.ind_j = self.bones[4].index(j)
                        if self.bones[4][self.ind_j].h > 15:
                            self.bones[4][self.ind_j] = Atk("white", "bone_s",
                                self.bones[4][self.bones[4].index(j)].x,
                                self.bones[4][self.bones[4].index(j)].y + 2.5,
                                self.bones[4][self.bones[4].index(j)].w,
                                self.bones[4][self.bones[4].index(j)].h - 2.5, False, 0)
                            self.bones[4][self.ind_j].ch_s = "second"

                    if self.bones.index(i) == 3:
                        if self.bones[3][self.ind_j].h > 100:
                            self.bones[3][self.ind_j].ch_s = "second"
                    if self.bones.index(i) == 4:
                        if self.bones[4][self.ind_j].h > 100:
                            self.bones[4][self.ind_j].ch_s = "second"
        if self.b2_sec == 314:
            self.bones = []
        if 60 <= self.b2_sec <= 150:
            self.all_platforms[0].moving(self.speed_b2, 0)
        if self.b2_sec == 105:
            player.change_gravity("up", True)
        if self.b2_sec == 77:
            self.blasters.append(Atk("white", "blaster", 300, 150, 60, 60, False, 360))
        if self.b2_sec == 135:
            player.change_gravity("down", True)
        if self.b2_sec == 140:
            self.blasters.append(Atk("white", "blaster", 100, 450, 60, 60, False, 90))
        if self.b2_sec == 300:
            sans.face = face[3]
        if 300 <= self.b2_sec <= 305:
            box.change_size(10, 0)
            sans.x += 65
        if 300 <= self.b2_sec <= 308:
            box.change_pos(-18, 0)
        if self.b2_sec == 300:
            self.blasters.append(Atk("white", "blaster", 500, 350, 60, 60, False, -90))
        if self.b2_sec == 300:
            player.change_gravity("left", True)
        if self.b2_sec == 315:
            player.mode = "red"
            for i in range(65):
                self.bones1.append(Atk("white", "bone_s", -30 - i * 25, 0, 10, 20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(65):
                self.bones1.append(Atk("white", "bone_s", -30 - i * 25, 180, 10, 20, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(6):
                self.bones1.append(Atk("white", "bone_s", -500 - i * 250, 100, 10, 100, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            for i in range(6):
                self.bones1.append(Atk("white", "bone_s", 500 + i * 250, 0, 10, 100, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
        if 315 <= self.b2_sec <= 500:
            for i in self.bones:
                for j in i:
                    if self.bones.index(i) in range(0, 3):
                        j.moving(self.speed_b2, 0)
                    if self.bones.index(i) == 3:
                        j.moving(-self.speed_b2, 0)
        if self.b2_sec == 420:
            self.blasters.append(Atk("white", "blaster", 400, 290, 60, 60, False, -90, 1.5, True))
            self.blasters.append(Atk("white", "blaster", 400, 410, 60, 60, False, -90, 1.5, True))
        if 380 <= self.b2_sec <= 418:
            box.change_pos(3, 0)
            box.w -= 20 / 38
        if 410 <= self.b2_sec <= 418:
            sans.x -= 20
        if self.b2_sec == 410:
            sans.face = face[1]

    def block2(self):
        self.b3_sec += 1
        if self.b3_sec == 1:
            for i in range(80):
                self.bones1.append(Atk("white", "bone_s", 520 + i * 22, 200, 10, 40, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            self.bones.append([Atk("white", "bone_s", 1080, 0, 10, 60, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1110, 0, 10, 80, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1140, 0, 10, 100, False, 0)])
            for i in range(3):
                self.bones1.append(Atk("white", "bone_s", 740 + i * 25, 0, 10, 60 - i * 10,
                    False, 0))
                self.bones1.append(Atk("white", "bone_s", 740 + i * 25, 120 - i * 10, 10,
                    120 + i * 10, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            self.bones.append([Atk("white", "bone_s", 1260, 60, 10, 180, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1280, 60, 10, 180, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1300, 60, 10, 180, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1430, 0, 10, 110, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1890, 95, 10, 150, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1913, 84, 10, 160, False, 0)])
            self.bones.append([Atk("white", "bone_s", 1936, 72, 10, 170, False, 0)])

            #Создаём платформы в разных координатах
            self.all_platforms.append(Platform(600, 180, 60, 11, "green"))
            self.all_platforms.append(Platform(1000, 100, 60, 11, "pink"))
            self.all_platforms.append(Platform(1100, 160, 60, 11, "pink"))
            self.all_platforms.append(Platform(1320, 80, 60, 11, "green"))
            self.all_platforms.append(Platform(1350, 180, 60, 11, "pink"))
            self.all_platforms.append(Platform(1760, 130, 60, 11, "pink"))
            self.all_platforms.append(Platform(1890, 70, 60, 11, "pink", 28))
            self.all_platforms.append(Platform(2150, 150, 60, 11, "green"))

        if self.b3_sec == 50:
            self.bone_str.append(Atk_comb())
            self.bone_str[0].bone_strike(50, "left", 1, 7, 15, False)

        if self.b3_sec == 285:
            self.blasters.append(Atk("white", "blaster", 380, 150, 60, 60, False, 0, 1.5, True))


        if 1 <= self.b3_sec <= 410:
            for i in self.bones:
                for j in i:
                    j.moving(-4.8, 0)
            for i in self.all_platforms:
                i.moving(-4.8, 0)
        if self.b3_sec == 410:
            self.all_platforms.append(Platform(-200, 90, 60, 11, "green"))
            self.all_platforms.append(Platform(-500, 180, 60, 11, "green"))
            self.all_platforms.append(Platform(-870, 90, 60, 11, "green"))
            self.all_platforms.append(Platform(-1500, 90, 60, 11, "green"))
            for i in range(50):
                self.bones1.append(Atk("white", "bone_s", -80 - i * 22, 0, 10, 30, False, 0))
            self.bones.append(self.bones1)
            self.bones1 = []
            self.bones.append([Atk("orange", "bone_s", -1250, 0, 10, 120, False, 0)])
            self.bones.append([Atk("orange", "bone_s", -1300, 0, 10, 120, False, 0)])
            self.bones.append([Atk("orange", "bone_s", -1350, 0, 10, 120, False, 0)])

        if 410 <= self.b3_sec <= 800:
            for i in [self.bones[0], self.bones[12], self.bones[13], self.bones[14],
                self.bones[15]]:
                for j in i:
                    j.moving(min((self.b3_sec - 419.6) / 2, 4.8), 0)
            for i in self.all_platforms:
                if self.all_platforms.index(i) >= 6:
                    i.moving(min((self.b3_sec - 419.6) / 2, 4.8), 0)
                else:
                    i.moving(-4.8, 0)
        if self.b3_sec == 705:
            player.change_gravity("up", True)

        if 450 <= self.b3_sec <= 500:
            box.change_pos(-1, 0)
        if self.b3_sec == 780:
            player.change_gravity("down", False)


    def atk2(self, sec):
        if sec % 15 == 0:
            self.blasters.append(Atk("white", "blaster", randint(0, 600), randint(0, 600),
                60, 60, True))

    def atkx(self, sec):
        for i in range(50):
            colo = randint(0, 2)
            if colo == 0:
                self.bones1.append(Atk("blue", "bone_s", -10 - i * 50, 100, 10, 200, False,
                    90, 1.05))
            if colo == 1:
                self.bones1.append(Atk("orange", "bone_s", -10 - i * 50, 100, 10, 200, False,
                    90, 1.05))
            if colo == 2:
                self.bones1.append(Atk("white", "bone_s", -10 - i * 50, 110, 10, 100, False,
                    0, 1.2))
            self.bones.append(self.bones1)
            self.bones1 = []

    def draw_blasters(self):
        ind = []
        for i in self.blasters:
            if i.draw():
                ind.append(self.blasters.index(i))

        for i in reversed(ind):
            del self.blasters[i]

    def draw_bones(self):
        pole = data.pole
        for i in self.bones:
            for j in i:
                pole.blit(j.bon, (j.x, j.y))
        for i in self.bone_str:
            for j in i.bone:
                pole.blit(j.bon, (j.x, j.y))

    def rotate_screen(self):
        screen.blit(rot(screen, sec)[0], rot(screen, sec)[1])

    def draw_shake(self):
        if self.shaker:
            x123, y123 = self.shaker.pop(0), self.shaker.pop(0)
            screen.blit(screen, (x123, y123))

    def clear(self):
        self.bones = []
        self.bones1 = []
        self.blasters = []
        self.bone_str = []
        self.all_platforms = []
        self.shaker = []
        self.change = False
        self.bool0 = False
        self.skip = False
        if data.sec <= 1:
            self.flag_fill_screen = False
            self.blok = False
            self.speed_b2 = 12
            self.fill_timer = 0
            self.b1_sec = 0
            self.b2_sec = 0
            self.b3_sec = 0

    def draw_fill(self):
        if self.fill_timer > 0:
            screen.fill(Color("black"))
            self.fill_timer -= 1

    def change_screen_scale(self):
        if self.c_h_bool:
            screen_n = pygame.transform.scale(screen, (600 + self.c_h, 600 + self.c_h))
            screen.fill(Color("black"))
            screen.blit(screen_n, (self.c_x, self.c_y))

    def draw_platforms(self):
        for i in self.all_platforms:
            i.draw()


def skip():
    global sec, sec1
    screen.set_alpha(255)
    data.sec = 1010
    sec, sec1 = 1010, 1010
    data.at.skip = True
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music/megalovania.mp3")
    pygame.mixer.music.play(-1, 1010 / 29)
    print(round(pygame.mixer.music.get_pos() / 1000 * 29))
    sans.face = face_ser
