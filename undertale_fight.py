# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wrong-import-order
# pylint: disable=no-member
# pylint: disable=invalid-name

import sys
import math
import os
import ctypes
import time
import pylint
import pygame
import data
import sys

from random import randint, uniform
from pygame import Color, Surface
from atk_list import AtkList
from functions import change_scale
from box import Box
from player import Player


def restart():
    global sec, fps, size, wx1, wy1, w2, h2, player, at, box, sans, diologs
    global quit_timer, name_entering, move_right, move_stop, timers, txt_ach, flex_gradient
    global flex_gradient_speed, bool_gradient
    if sec == -9:
        pygame.mixer.music.stop()
        intro.play()
    elif sec >= 0 or sec == -2:
        data.sec = sec = 0
        pygame.mixer.music.load("music/megalovania.mp3")
        pygame.mixer.music.play(-1)
    data.end = False
    quit_timer = -1
    name_entering = ""
    move_right = True
    move_stop = False
    flex_gradient = 140
    flex_gradient_speed = 5
    bool_gradient = 1
    fps = 29
    timers = 0
    txt_ach = ""
    size = (600, 600)
    wx1, wy1, w2, h2 = 200, 300, 200, 200
    screen.fill(Color("black"))
    data.sans = sans = Sans()
    data.player = player = Player()
    data.at = at = AtkList()
    data.box = box = Box(wx1, wy1, w2, h2)
    data.diologs = diologs = Diologs()
    pygame.display.flip()
    restart_txts()
    wallues()

def change_screen():
    global scr, screen1
    if scr == "small":
        scr = "full"
        pygame.display.quit()
        pygame.display.init()
        screen1 = pygame.display.set_mode((monitorsize))
    elif scr == "full":
        scr = "small"
        pygame.display.quit()
        pygame.display.init()
        screen1 = pygame.display.set_mode(size)

def change_wods_place(words_t1):
    global name_entering, run, sec, timers, screen_x1, timers1, mus
    global language, all_txts, name
    if timers1 == 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                for i in range(len(words_t1)):
                    for j in range(len(words_t1[i])):
                        if "1" in words_t1[i][j]:
                            words_t1[i][j] = words_t1[i][j].replace("1", "")
                            minus_j = j - 1
                            if words_t1[i][minus_j] == "":
                                word_t1 = words_t1
                                f = 0
                                while word_t1[i][minus_j - f] == "":
                                    f += 1
                                minus_j -= f
                                words_t1[i][minus_j] += "1"
                                break
                            words_t1[i][minus_j] += "1"
                            if minus_j == -1:
                                break
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                for i in range(len(words_t1)):
                    for j in range(len(words_t1[i])):
                        if "1" in words_t1[i][j]:
                            words_t1[i][j] = words_t1[i][j].replace("1", "")
                            minus_j = j + 1
                            if minus_j >= len(words_t1[0]):
                                minus_j = 0
                            if words_t1[i][minus_j] == "":
                                words_t1[i][minus_j] += "1"
                                continue
                            words_t1[i][minus_j] += "1"
                            break
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                bool_stop = False
                for i in range(len(words_t1)):
                    for j in range(len(words_t1[i])):
                        if "1" in words_t1[i][j]:
                            words_t1[i][j] = words_t1[i][j].replace("1", "")
                            minus_i = i + 1
                            if sec == -10 and minus_i == 8:
                                if j in (0, 1):
                                    j = 0
                                if j in (2, 3, 4):
                                    j = 2
                                if j in (5, 6):
                                    j = 5
                                words_t1[minus_i][j] += "1"
                                bool_stop = True
                                break
                            if minus_i >= len(words_t1):
                                minus_i = 0
                            if words_t1[minus_i][j] == "":
                                words_t1[minus_i][j] += "1"
                                continue
                            words_t1[minus_i][j] += "1"
                            bool_stop = True
                            break
                    if bool_stop:
                        break
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                bool_stop = False
                for i in range(len(words_t1)):
                    for j in range(len(words_t1[i])):
                        if "1" in words_t1[i][j]:
                            words_t1[i][j] = words_t1[i][j].replace("1", "")
                            minus_i = i - 1
                            if words_t1[minus_i][j] == "":
                                if sec == -10 and minus_i == -1:
                                    if j in (0, 1):
                                        j = 0
                                    if j in (2, 3, 4):
                                        j = 2
                                    if j in (5, 6):
                                        j = 5
                                    words_t1[minus_i][j] += "1"
                                    bool_stop = True
                                    break

                                word_t1 = words_t1
                                f = 0
                                while word_t1[minus_i - f][j] == "":
                                    f += 1
                                words_t1[minus_i - f][j] += "1"
                                bool_stop = True
                                break
                            words_t1[minus_i][j] += "1"
                            if minus_i == -1:
                                bool_stop = True
                                break
                    if bool_stop:
                        break
            if event.key == pygame.K_RETURN or event.key == pygame.K_z:
                if sec == -11:
                    for i in words_t1[0]:
                        if "1" in i:
                            if i == all_txts[35] + "1":
                                file[1] = name_entering
                                file[2] = "False"
                                name = name_entering
                                open("resours/data.txt", "w").write("\n".join(file))
                                sec = -20
                                break
                            if i == all_txts[34] + "1":
                                timers = 0
                                sec = -10
                elif sec == -10:
                    for i in words_t1:
                        for j in i:
                            if "1" in j:
                                if j == all_txts[36] + "1":
                                    name_entering = name_entering[0:len(name_entering) - 1]
                                    break
                                if j == all_txts[32] + "1":
                                    sec = -8
                                    name_entering = ""
                                    break
                                if j == all_txts[37] + "1":
                                    if len(name_entering) > 0:
                                        sec = -11
                                    break
                                if len(name_entering) < 6:
                                    name_entering += j.replace("1", "")
                elif sec == -8:
                    for j in words_t1:
                        for i in j:
                            if "1" in i:
                                if i == all_txts[33] + "1":
                                    sec = -10
                                if i == all_txts[32] + "1":
                                    run = False
                elif sec == -20:
                    for i in words_t1:
                        for j in i:
                            if "1" in j:
                                if j == all_txts[28] + "1":
                                    sec = 0
                                elif j == all_txts[29] + "1":
                                    screen_x1 = Surface((600, 600))
                                    screen_x1.blit(screen, (0, 0))
                                    timers1 = 30
                                    sec = -21
                                elif j == all_txts[30] + "1":
                                    screen_x1 = Surface((600, 600))
                                    screen_x1.blit(screen, (0, 0))
                                    timers1 = 30
                                    sec = -22
                                elif j == all_txts[31] + "1":
                                    sec = -23
                                elif j == all_txts[32] + "1":
                                    run = False
                elif sec == -21:
                    for i in words_t1:
                        for j in i:
                            if "1" in j:
                                if j == all_txts[23] + "1":
                                    screen_x1 = Surface((600, 600))
                                    screen_x1.blit(screen, (0, 0))
                                    timers1 = 30
                                    sec = -20
                                elif j == all_txts[24] + "1":
                                    print(mus)
                                    if pygame.mixer.music.get_volume() == 1.0:
                                        pygame.mixer.music.set_volume(0)
                                    else:
                                        pygame.mixer.music.set_volume(1)
                                    mus = pygame.mixer.music.get_volume()
                                    file[4] = str(int(mus))
                                    print(file)
                                    open("resours/data.txt", "w").write("\n".join(file))
                                elif j == all_txts[26] + "1":
                                    pass
                                elif j == all_txts[27] + "1":
                                    open("resours/data.txt", "w").write(
                                        "".join(open("resours/data_0.txt")))
                                    sec = -9
                                    restart()
                                elif j == all_txts[25] + "1":
                                    if language == "ru":
                                        language = "eng"
                                        data.all_txts = all_txts = open(
                                            "resours/languages/eng.txt").read().split("\n")
                                        file
                                    elif language == "eng":
                                        language = "ru"
                                        data.all_txts = all_txts = open(
                                            "resours/languages/ru.txt").read().split("\n")
                                    file[3] = language
                                    file_0 = open("resours/data_0.txt").read().split("\n")
                                    file_0[3] = language
                                    open("resours/data_0.txt", "w").write("\n".join(file_0))
                                    open("resours/data.txt", "w").write("\n".join(file))
                                    restart_txts()
                elif sec == -22:
                    if "1" in words_t1[0][0]:
                        screen_x1 = Surface((600, 600))
                        screen_x1.blit(screen, (0, 0))
                        timers1 = 30
                        sec = -20

                elif sec == -23:
                    sec = -20


class Sans():
    def __init__(self):
        self.sans = Surface((200, 200), pygame.SRCALPHA, 32)
        self.x, self.y = 215, 140
        self.x_f, self.y_f = 50, 13
        self.x_t, self.y_t = 28, 61
        self.x_l, self.y_l = 40, 110
        self.face = face[4]
        self.tors = tors_1
        self.mov = False
        self.face_move = [12, 12, 13, 13]
        self.face_move2 = [11, 9, 6, 9, 11]
        self.body_move = []
        self.time = 0
        self.hand_time = 0
        self.hand_down_bool = False
        self.hand_up_bool = False
        self.hand_right_bool = False

    def draw(self):
        self.sans = Surface((200, 200), pygame.SRCALPHA, 32)
        if self.hand_down_bool:
            self.hand_down()
            self.sans.blit(self.body, (25, 15))
        elif self.hand_up_bool:
            self.hand_up()
            self.sans.blit(self.body, (25, 15))
        elif self.hand_right_bool:
            self.hand_right()
            self.sans.blit(self.body, (15, 60))
        else:
            self.sans.blit(self.tors, (self.x_t, self.y_t))
            self.sans.blit(legs, (self.x_l, self.y_l))
        self.sans.blit(self.face, (self.x_f, self.y_f))
        screen.blit(self.sans, (self.x, self.y))

    def move_body(self):
        if self.mov:
            self.time += 1
            if self.time % 5 == 0:
                self.y_f = self.face_move[self.time % 4]
                if self.time % 40 < 20:
                    self.x_t -= 1
                    self.x_f -= 1
                else:
                    self.x_t += 1
                    self.x_f += 1
                if self.time % 2 == 0:
                    if self.time % 20 < 10:
                        self.y_t -= 1
                        self.y_f -= 0.5
                    else:
                        self.y_t += 1
                        self.y_f += 0.5
        else:
            self.x_f, self.y_f = 50, 13
            self.x_t, self.y_t = 28, 61
            self.x_l, self.y_l = 40, 110

    def hand_down(self):
        if self.hand_time < 5:
            self.body = hand_down[self.hand_time]
            self.y_f = self.face_move2[self.hand_time]
            self.hand_time += 1
        else:
            self.hand_time = 0
            self.hand_down_bool = False

    def hand_up(self):
        if self.hand_time < 5:
            self.body = hand_up[self.hand_time]
            self.y_f = self.face_move2[self.hand_time]
            self.hand_time += 1
        else:
            self.hand_time = 0
            self.hand_up_bool = False

    def hand_right(self):
        if self.hand_time < 5:
            self.body = hand_right[self.hand_time]
            self.x_f = self.face_move2[self.hand_time] + 35
            self.hand_time += 1
        else:
            self.hand_time = 0
            self.hand_right_bool = False
            self.x_f = 48



class Diologs():
    def __init__(self):
        self.time, self.txt, self.txt2, self.txt1 = 0, "", "", ""
        self.next, self.stop = False, False

    def draw_all(self, x, y, voice=True):
        screen.blit(dio1, (x, y))
        if "=" == self.txt[self.time]:
            self.next = True
            t = f3.render(self.txt1, True, Color("black"))
            screen.blit(t, (x + 35, y + 15))
            self.time += 1
            if voice:
                s_voice.stop()
                s_voice.play()
            return
        t = f3.render(self.txt1, True, Color("black"))
        if self.next:
            if not self.stop:
                self.txt2 += self.txt[self.time]
                if voice:
                    s_voice.stop()
                    s_voice.play()
            t1 = f3.render(self.txt2, True, Color("black"))
            screen.blit(t1, (x + 35, y + 35))
        if not self.next and not self.stop:
            self.txt1 += self.txt[self.time]
            if voice:
                s_voice.stop()
                s_voice.play()
        screen.blit(t, (x + 35, y + 15))
        if self.time < len(self.txt) - 1:
            self.time += 1
        else:
            self.stop = True


def restart_txts():
    global words_t1, words_t2, words_t3, words_t4, words_settings, words_extras, words_achievements
    words_t1 = [["A1", "B", "C", "D", "E", "F", "G"],
        ["H", "I", "J", "K", "L", "M", "N"],
        ["O", "P", "Q", "R", "S", "T", "U"],
        ["V", "W", "X", "Y", "Z", "", ""],
        ["a", "b", "c", "d", "e", "f", "g"],
        ["h", "i", "j", "k", "l", "m", "n"],
        ["o", "p", "q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z", "", ""],
        [all_txts[32], "", all_txts[36], "", "", all_txts[37], ""]]

    words_t2 = [[all_txts[34] + "1", all_txts[35]]]
    words_t3 = [[all_txts[33] + "1"], [all_txts[32]]]
    words_t4 = [[all_txts[28] + "1"], [all_txts[29]], [all_txts[30]], [all_txts[31]],
        [all_txts[32]]]
    words_settings = [[all_txts[23] + "1"], [all_txts[24]], [all_txts[25]], [all_txts[26]],
        [all_txts[27]]]
    words_extras = [[all_txts[23] + "1"]]
    words_achievements = [[all_txts[23] + "1", "", "", ""],
        ["first", "second", "third", "fourth"], ["fifth", "sixth", "seventh", "eighth"]]

def wallues():
    global file, death, name, new_game, mus, language, all_txts
    data.file = file = open("resours/data.txt").read().split("\n")
    data.death = death = int(file[0])
    name = file[1]
    new_game = file[2]
    language = file[3]
    mus = float(file[4])
    if language == "eng":
        all_txts = open("resours/languages/eng.txt", encoding="ANSI").read().split("\n")
    if language == "ru":
        all_txts = open("resours/languages/ru.txt", encoding="ANSI").read().split("\n")
    print(all_txts)

def change_menu(screen1, screen2):
    global timers1
    if timers1 > 0:
        screen.fill(Color("black"))
        screen.blit(screen1, (0 - (30 - timers1) * 1200 / 30, 0))
        screen.blit(screen2, (1200 - (30 - timers1) * 1200 / 30, 0))
        timers1 -= 1



if __name__ == '__main__':
    run = True
    data.end = False
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    scr = "small"
    quit_timer = -1
    timers1 = 0
    n = 2
    g = 0.2
    name_entering = ""
    move_right = True
    move_stop = False
    data.sec = sec = -9
    fps = 29
    size = (600, 600)
    timers = 0
    stop_change = False
    move_down = True
    change_menu_bool = False
    txt_ach = ""
    wx1, wy1, w2, h2 = 200, 300, 200, 200
    x_flex = 0
    x_soul_menu, y_soul_menu = 35, 103
    flex_gradient = 140
    flex_gradient_speed = 5
    bool_gradient = 1
    col_2, col_3 = 255, 255
    time_global_hour = int(time.strftime("%H"))
    screen_x1, screen_x2 = [], []
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()
    screen1 = pygame.display.set_mode(size)
    screen = Surface(size)
    screen.fill(Color("black"))
    data.screen1, data.screen = screen1, screen



    ## Изменение меню ##
    words_change_x_menu = [0, 0, 0, 0, 0]
    words_change_x_settings = [0, 0, 0, 0, 0]

    ## Разрешение экрана ##
    user32 = ctypes.windll.user32
    monitorsize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

    ## Шрифты ##
    data.f1 = f1 = pygame.font.Font("resours/abs.ttf", 15)
    f2 = pygame.font.Font("resours/sans.ttf", 15)
    f3 = pygame.font.Font("resours/sans.ttf", 16)
    f4 = pygame.font.Font("resours/abs.ttf", 12)
    f5 = pygame.font.Font("resours/determ.otf", 30)
    f7 = pygame.font.Font("resours/determ.otf", 26)

    data.track = track = pygame.image.load("resours/Track.png").convert()
    data.blast = blast = pygame.image.load("resours/Blaster1.png").convert()
    data.blast_open = blast_open = pygame.image.load("resours/Blaster_open1.png").convert()
    data.blast_open2 = blast_open2 = pygame.image.load("resours/Blaster_open2.png").convert()
    data.blast_open3 = blast_open3 = pygame.image.load("resours/Blaster_open3.png").convert()
    data.red_soul = red_soul = pygame.image.load("resours/Red_soul.png").convert()
    data.blue_down = blue_down = pygame.image.load("resours/Blue_soul_down.png").convert()
    data.blue_up = blue_up = pygame.image.load("resours/Blue_soul_up.png").convert()
    data.blue_left = blue_left = pygame.image.load("resours/Blue_soul_left.png").convert()
    data.blue_right = blue_right = pygame.image.load("resours/Blue_soul_right.png").convert()

    ## Градиент ##
    gr_game = bone_white = pygame.image.load("resours/gradient.png").convert_alpha()
    gr_game_up = bone_white = pygame.image.load("resours/gradient_up.png").convert_alpha()

    ## Разделённые кости ##
    data.bone_up = bone_up = pygame.image.load("resours/Bone_up.png").convert()
    data.bone_middle = bone_middle = pygame.image.load("resours/Bone_middle.png").convert()
    data.bone_down = bone_down = pygame.image.load("resours/Bone_down.png").convert()
    data.bone_up_orange = bone_up_orange = pygame.image.load(
        "resours/Bone_up_orange.png").convert()
    data.bone_middle_orange = bone_middle_orange = pygame.image.load(
        "resours/Bone_middle_orange.png").convert()
    data.bone_down_orange = bone_down_orange = pygame.image.load(
        "resours/Bone_down_orange.png").convert()
    data.bone_up_blue = bone_up_blue = pygame.image.load("resours/Bone_up_blue.png").convert()
    data.bone_middle_blue = bone_middle_blue = pygame.image.load(
        "resours/Bone_middle_blue.png").convert()
    data.bone_down_blue = bone_down_blue = pygame.image.load(
        "resours/Bone_down_blue.png").convert()

    ## Кнопки ##
    fight = pygame.image.load("resours/Fight.png").convert()
    act = pygame.image.load("resours/Act.png").convert()
    item = pygame.image.load("resours/Item.png").convert()
    mercy = pygame.image.load("resours/Mercy.png").convert()

    ## Ачивки ##
    ach_hide = pygame.image.load("resours/achievement_hide.png").convert()
    ach_hide_yel = pygame.image.load("resours/achievement_hide_yellow.png").convert()

    ## Сломанная душа ##
    data.broken_soul = broken_soul = pygame.image.load("resours/broken_soul.png").convert()
    soul_part1 = pygame.image.load("resours/soul_part1.png").convert()
    soul_part2 = pygame.image.load("resours/soul_part2.png").convert()
    soul_part3 = pygame.image.load("resours/soul_part3.png").convert()
    data.soul_parts = soul_parts = [soul_part1, soul_part2, soul_part3]

    ## Платформы ##
    data.plat_green = pygame.image.load("resours/green_platform.png").convert()
    data.plat_pink = pygame.image.load("resours/pink_platform.png").convert()

    ## Диологовые окна ##
    dio1 = pygame.image.load("resours/diolog_1.png").convert()

    ## Конец игры ##
    data.GO = GO = change_scale(pygame.image.load("resours/game_over.jpg").convert_alpha(), 5, 5)
    GO.set_colorkey(Color("black"))

    ## Заставка ##
    Undertale_title = change_scale(pygame.image.load(
        "resours/Undertale_title.png").convert_alpha(), 5, 5)

    ## Локации, меню ##
    colonna = pygame.transform.scale(pygame.image.load("resours/colonna.png"), (150.75, 450))
    gr_men_d = pygame.image.load("resours/down_menu_gradient.png")
    if 7 <= time_global_hour < 17:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_day_menu.png"), (2700, 450))
    if time_global_hour == 17:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_17_00_menu.png"), (2700, 450))
    if time_global_hour == 18:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_18_00_menu.png"), (2700, 450))
    if time_global_hour == 19:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_19_00_menu.png"), (2700, 450))
    if time_global_hour == 20:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_20_00_menu.png"), (2700, 450))
    if time_global_hour == 21:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_21_00_menu.png"), (2700, 450))
    if time_global_hour == 22:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_22_00_menu.png"), (2700, 450))
    if 0 <= time_global_hour < 7 or 22 < time_global_hour < 24:
        corridor_menu_day = pygame.transform.scale(pygame.image.load(
            "resours/last_corridor_night_menu.png"), (2700, 450))

    ## Звуки ##
    data.hit_s = hit_s = pygame.mixer.Sound('sounds/hit.wav')
    data.hit1_s = hit1_s = pygame.mixer.Sound('sounds/hit1.wav')
    data.blaster_start_s = blaster_start_s = pygame.mixer.Sound('sounds/blaster_start.ogg')
    data.blaster_end_s = blaster_end_s = pygame.mixer.Sound('sounds/blaster_end.ogg')
    data.blim_s = blim_s = pygame.mixer.Sound('sounds/bong.wav')
    data.break1_s = break1_s = pygame.mixer.Sound('sounds/break1.wav')
    data.break2_s = break2_s = pygame.mixer.Sound('sounds/break2.wav')
    data.bam = bam = pygame.mixer.Sound('sounds/bam.wav')
    data.s_voice = s_voice = pygame.mixer.Sound('sounds/sans_txt.wav')
    data.intro = intro = pygame.mixer.Sound("sounds/intro.ogg")

    ## ----------- SANS ----------- ##
    ## legs ##
    data.legs = legs = change_scale(pygame.image.load("resours/sans/legs.png").convert())

    ## tors ##
    data.tors_1 = tors_1 = change_scale(pygame.image.load("resours/sans/tors_1.png").convert())
    data.tors_2 = tors_2 = change_scale(pygame.image.load("resours/sans/tors_2.png").convert())

    ## face ##
    face_1 = change_scale(pygame.image.load("resours/sans/face_1.png").convert())
    face_2 = change_scale(pygame.image.load("resours/sans/Face_2.png").convert())
    face_3 = change_scale(pygame.image.load("resours/sans/Face_3.png").convert())
    face_4 = change_scale(pygame.image.load("resours/sans/Face_4.png").convert())
    face_5 = change_scale(pygame.image.load("resours/sans/Face_5.png").convert())
    face_eye_1 = change_scale(pygame.image.load("resours/sans/Face_eye_blue.png").convert())
    face_eye_2 = change_scale(pygame.image.load("resours/sans/Face_eye_yellow.png").convert())
    data.face_ser = face_ser = change_scale(pygame.image.load(
        "resours/sans/Face_seriose.png").convert())
    data.face = face = [face_1, face_2, face_3, face_4, face_5]
    data.face_eye = face_eye = [face_eye_1, face_eye_2]
    ## hand_down ##
    h_down_1 = change_scale(pygame.image.load("resours/sans/hand_down_1.png").convert())
    h_down_2 = change_scale(pygame.image.load("resours/sans/hand_down_2.png").convert())
    h_down_3 = change_scale(pygame.image.load("resours/sans/hand_down_3.png").convert())
    h_down_4 = change_scale(pygame.image.load("resours/sans/hand_down_4.png").convert())
    h_down_5 = change_scale(pygame.image.load("resours/sans/hand_down_5.png").convert())
    data.hand_down = hand_down = [h_down_1, h_down_2, h_down_3, h_down_4, h_down_5]

    ## hand_up ##
    h_up_1 = change_scale(pygame.image.load("resours/sans/hand_up_1.png").convert())
    h_up_2 = change_scale(pygame.image.load("resours/sans/hand_up_2.png").convert())
    h_up_3 = change_scale(pygame.image.load("resours/sans/hand_up_3.png").convert())
    h_up_4 = change_scale(pygame.image.load("resours/sans/hand_up_4.png").convert())
    h_up_5 = change_scale(pygame.image.load("resours/sans/hand_up_5.png").convert())
    data.hand_up = hand_up = [h_up_1, h_up_2, h_up_3, h_up_4, h_up_5]

    ## hand_right ##
    h_right_1 = change_scale(pygame.image.load("resours/sans/hand_right_1.png").convert())
    h_right_2 = change_scale(pygame.image.load("resours/sans/hand_right_2.png").convert())
    h_right_3 = change_scale(pygame.image.load("resours/sans/hand_right_3.png").convert())
    h_right_4 = change_scale(pygame.image.load("resours/sans/hand_right_4.png").convert())
    h_right_5 = change_scale(pygame.image.load("resours/sans/hand_right_5.png").convert())
    data.hand_right = hand_right = [h_right_1, h_right_2, h_right_3, h_right_4, h_right_5]

    ## ----------------------------- ##
    data.sans = sans = Sans()

    ## Значения ##
    wallues()
    pygame.mixer.music.set_volume(mus)

    ## ---------- Тексты ---------- ##
    restart_txts()

    data.all_txts = all_txts

    player = Player()
    data.at = at = AtkList()
    box = Box(wx1, wy1, w2, h2)
    diologs = Diologs()
    data.diologs, data.player, data.box, data.sans = diologs, player, box, sans
    pygame.display.flip()

    intro.play()


    while run:
        clock.tick(fps)
        pygame.display.set_caption(f"Fps {clock.get_fps()}")
        if data.end == True:
            sec = -1000
        if sec == 0:
            pygame.mixer.music.load("music/megalovania.mp3")
            pygame.mixer.music.play(-1)
        if sec >= 0:
            data.sec += 1
            sec += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if player.check_death():
                if player.sec_d > 200:
                    if event.type == pygame.KEYDOWN:
                        restart()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    change_screen()
                if event.key == pygame.K_ESCAPE:
                    quit_timer = 0
                if sec >= 0 or sec == -2:
                    if event.key == pygame.K_DELETE:
                        restart()
                if sec == -9:
                    if event.key in (pygame.K_RETURN, event.key == pygame.K_z):
                        intro.stop()
                        timers = 0
                        stop_change = True
                        if new_game == "True":
                            sec = -8
                            pygame.mixer.music.load("music/start_menu.mp3")
                            pygame.mixer.music.play(-1)
                        else:
                            sec = -20
                if sec == -1000:
                    if event.key in (pygame.K_RETURN, event.key == pygame.K_z):
                        data.sec = sec = -9
                        intro.play()
                        pygame.mixer.music.stop()
                        restart()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    quit_timer = -1
            if sec == -10:
                change_wods_place(words_t1)
            elif sec == -11:
                change_wods_place(words_t2)
            elif sec == -8:
                if stop_change is False:
                    change_wods_place(words_t3)
                stop_change = False
            elif sec == -20:
                if stop_change is False:
                    change_wods_place(words_t4)
                stop_change = False
            elif sec == -21:
                if stop_change is False:
                    change_wods_place(words_settings)
                stop_change = False
            elif sec == -22:
                change_wods_place(words_achievements)
            elif sec == -23:
                change_wods_place(words_t1)


        if player.check_death() is False and sec >= 0:
            if at.blok:
                press = pygame.key.get_pressed()
                if press[pygame.K_LEFT] or press[pygame.K_a]:
                    player.movement(-1, 0, "right")
                elif not(press[pygame.K_LEFT] or press[pygame.K_a]):
                    player.jum("right")
                if press[pygame.K_RIGHT] or press[pygame.K_d]:
                    player.movement(1.3, 0, "left")
                elif not(press[pygame.K_RIGHT] or press[pygame.K_d]):
                    player.jum("left")
                if press[pygame.K_DOWN] or press[pygame.K_s]:
                    player.movement(0, 1.3, "up")
                elif not(press[pygame.K_DOWN] or press[pygame.K_s]):
                    player.jum("up")
                if press[pygame.K_UP] or press[pygame.K_w]:
                    player.movement(0, -1, "down")
                elif not(press[pygame.K_UP] or press[pygame.K_w]):
                    player.jum("down")


                if (not(press[pygame.K_LEFT] or press[pygame.K_a]) and not(press[pygame.K_RIGHT]
                    or press[pygame.K_d]) and not(press[pygame.K_DOWN] or press[pygame.K_s]) and
                    not(press[pygame.K_UP] or press[pygame.K_w])):
                    player.move = False
                if (press[pygame.K_UP] or press[pygame.K_w]) and (press[pygame.K_DOWN] or
                    press[pygame.K_s]):
                    player.move = False
                if (press[pygame.K_RIGHT] or press[pygame.K_d]) and (press[pygame.K_LEFT] or
                    press[pygame.K_a]):
                    player.move = False

            if player.ret_type() == "blue":
                player.phizic(g)

            player.check_box1()
            screen.fill(Color("black"))

            if data.sec >= 480:
                if data.sec % 10 == 0:
                    if bool_gradient == 0:
                        flex_gradient_speed += 1
                    elif bool_gradient == 1:
                        flex_gradient_speed -= 1
                if flex_gradient_speed <= -3:
                    bool_gradient = 0
                elif flex_gradient_speed >= 3:
                    bool_gradient = 1
                flex_gradient += flex_gradient_speed

                screen.blit(gr_game, (0, 310 + flex_gradient))
                screen.blit(gr_game_up, (0, 150 - flex_gradient))
            screen.blit(fight, (30, 550))
            screen.blit(act, (175, 550))
            screen.blit(item, (315, 550))
            screen.blit(mercy, (460, 550))
            pygame.draw.rect(screen, Color("red"), (260, 515, 120, 20))
            pygame.draw.rect(screen, (255, 0, 255), (260, 515, 120 / 92 * player.krhp, 20))
            pygame.draw.rect(screen, Color("yellow"), (260, 515, 120 / 92 * player.hp, 20))

            name_t = f1.render(name, True, Color("white"))
            screen.blit(name_t, (30, 515))

            LV_t = f1.render(all_txts[38] + " 19", True, Color("white"))
            screen.blit(LV_t, (130, 515))

            HP_t = f4.render(all_txts[39], True, Color("white"))
            screen.blit(HP_t, (230, 517))

            kr_t = f4.render(all_txts[40], True, Color("white"))
            screen.blit(kr_t, (390, 517))

            if player.hp == player.krhp:
                hp_kolv_t = f1.render(f"{player.hp} / 92", True, Color("white"))
                screen.blit(hp_kolv_t, (430, 515))
            else:
                hp_kolv_t = f1.render(f"{player.krhp} / 92", True, (255, 0, 255))
                screen.blit(hp_kolv_t, (430, 515))


            sans.draw()
            sans.move_body()
            box.start()
            at.draw_bones()
            at.all_atks()
            at.draw_platforms()
            box.surf()
            at.draw_blasters()

            player.hit()
            player.draw_player()
            player.change_color()
            at.draw_shake()
            at.draw_fill()
            if at.change:
                screen.fill(Color("black"))
            at.change_screen_scale()
        if sec <= -8:
            screen.fill(Color("black"))
        if sec == -10:
            n_f_h_t = f5.render(all_txts[0], True, Color("white"))
            screen.blit(n_f_h_t, (115, 100))
            fiv_ots = 0
            for i in range(len(words_t1)):
                for j in range(len(words_t1[i])):
                    word_t1 = words_t1[i][j]
                    if "1" in word_t1:
                        word_t1 = word_t1.replace("1", "")
                        color_text = "yellow"
                    else:
                        color_text = "white"
                    word_t1 = f5.render(word_t1, True, Color(color_text))
                    if i > 3:
                        fiv_ots = 10
                    if i > 7:
                        fiv_ots = 30
                    x, y = 55 + j * 80, 220 + i * 30 + fiv_ots
                    if words_t1[i][j] == "Стереть" or words_t1[i][j] == "Стереть1":
                        x = 240
                    if i <= 7:
                        x += randint(-1, 1)
                        y += randint(-1, 1)
                    screen.blit(word_t1, (x, y))
            name_ent = f5.render(name_entering, True, Color(color_text))
            screen.blit(name_ent, (250, 170))
        if sec == -11:
            timers += 1
            txt_t_hallo = f5.render(all_txts[1], True, Color("white"))
            if language == "ru":
                screen.blit(txt_t_hallo, (170, 100))
            else:
                screen.blit(txt_t_hallo, (150, 100))
            f_x = pygame.font.Font("resours/determ.otf", 30 + math.ceil(timers * 0.4))
            name_ent = f_x.render(name_entering, True, Color("white"))
            timers = min(timers, 120)
            if timers == 120:
                name_ent = pygame.transform.rotate(name_ent, uniform(-0.8, 0.8))
            screen.blit(name_ent, (250 - timers * 0.7, 180 + timers))
            for i in words_t2[0]:
                word_t2 = i
                if "1" in i:
                    color_text = "yellow"
                    word_t2 = i.replace("1", "")
                else:
                    color_text = "white"
                word_t2 = f5.render(word_t2, True, Color(color_text))
                screen.blit(word_t2, (100 + words_t2[0].index(i) * 350, 500))
        if sec == -9:
            timers += 1
            undertale_title1 = pygame.transform.scale(Undertale_title, (500,
                Undertale_title.get_size()[1] - 10))
            screen.blit(undertale_title1, (50, 250))
            if timers == 60:
                intro.play()
            if timers >= 60:
                undertale_title2 = f7.render("LAST CHANCE", True, Color("white"))
                screen.blit(undertale_title2, (220, 350))
            if timers >= 150:
                f10 = pygame.font.Font("resours/determ.otf", 16)
                ins_t_1 = f10.render(all_txts[2], True, Color("gray"))
                screen.blit(ins_t_1, (228, 550))
        if sec == -8:
            instructions = f7.render(all_txts[3], True, Color("gray"))
            ins_t_1 = f7.render(all_txts[4], True, Color("gray"))
            ins_t_2 = f7.render(all_txts[5], True, Color("gray"))
            ins_t_3 = f7.render(all_txts[6], True, Color("gray"))
            ins_t_4 = f7.render(all_txts[7], True, Color("gray"))
            ins_t_5 = f7.render(all_txts[8], True, Color("gray"))
            ins_t_6 = f7.render(all_txts[9], True, Color("gray"))
            screen.blit(instructions, (150, 100))
            screen.blit(ins_t_1, (150, 150))
            screen.blit(ins_t_2, (150, 190))
            screen.blit(ins_t_3, (150, 230))
            screen.blit(ins_t_4, (150, 270))
            screen.blit(ins_t_5, (150, 310))
            screen.blit(ins_t_6, (155, 350))
            word_t3 = ""
            for i in words_t3:
                for j in i:
                    if "1" in j:
                        word_t3 = j.replace("1", "")
                        color_text = "yellow"
                    else:
                        word_t3 = j
                        color_text = "white"
                    word_t3 = f7.render(word_t3, True, Color(color_text))
                    screen.blit(word_t3, (155, 430 + 50 * words_t3.index(i)))
        if -20 >= sec >= -30:
            screen.blit(corridor_menu_day, (100 - x_flex, 0))
            for i in range(7):
                screen.blit(colonna, (350 + i * 550 - x_flex * 1.5, 0))
            if x_flex > 2400:
                move_right = False
                x_flex = 2400
                move_stop = True
                timers = 100
            elif x_flex < -100:
                move_right = True
                x_flex = -100
                move_stop = True
                timers = 100
            if move_right and not move_stop:
                x_flex += 2
            elif not move_right and not move_stop:
                x_flex -= 2
            if move_stop:
                timers -= 1
                if timers == 0:
                    move_stop = False
            screen.blit(gr_men_d, (0, 500))
            font1 = pygame.font.Font("resours/sans.ttf", 1)
            version = f7.render("v. 0.2.1", True, Color("gray"))
            screen.blit(version, (520, 0))


        if sec == -20:
            pygame.mixer.music.stop()
            for i in words_t4:
                for j in i:
                    if "1" in j:
                        word_t4 = j.replace("1", "")
                        color_text = "yellow"
                    else:
                        word_t4 = j
                        color_text = "white"
                    word_t4 = f7.render(word_t4, True, Color(color_text))
                    if "1" in j:
                        if words_change_x_menu[words_t4.index(i)] < 30:
                            words_change_x_menu[words_t4.index(i)] += 2
                        if y_soul_menu > 103 + words_t4.index(i) * 60:
                            y_soul_menu -= 10
                        elif y_soul_menu < 103 + words_t4.index(i) * 60:
                            y_soul_menu += 10
                        if y_soul_menu in range(107 + words_t4.index(i) * 60, 109 +
                            words_t4.index(i) * 60):
                            y_soul_menu = 103 + words_t4.index(i) * 60
                    else:
                        if words_change_x_menu[words_t4.index(i)] > 0:
                            words_change_x_menu[words_t4.index(i)] -= 2
                    screen.blit(word_t4, (50 + words_change_x_menu[words_t4.index(i)], 100 +
                        words_t4.index(i) * 60))
                    screen.blit(pygame.transform.scale(red_soul, (20, 20)), (x_soul_menu,
                        y_soul_menu))
        if sec == -21:
            for i in words_settings:
                for j in i:
                    if "1" in j:
                        word_set = j.replace("1", "")
                        color_text = "yellow"
                    else:
                        word_set = j
                        color_text = "white"
                    word_set = f7.render(word_set, True, Color(color_text))
                    if "1" in j:
                        if words_change_x_settings[words_settings.index(i)] < 30:
                            words_change_x_settings[words_settings.index(i)] += 2
                        if y_soul_menu > 83 + words_settings.index(i) * 60:
                            y_soul_menu -= 10
                        elif y_soul_menu < 83 + words_settings.index(i) * 60:
                            y_soul_menu += 10
                        if y_soul_menu in range(77 + words_settings.index(i) * 60, 89 +
                            words_settings.index(i) * 60):
                            y_soul_menu = 83 + words_settings.index(i) * 60
                    else:
                        if words_change_x_settings[words_settings.index(i)] > 0:
                            words_change_x_settings[words_settings.index(i)] -= 2
                    screen.blit(word_set, (50 + words_change_x_settings[words_settings.index(i)],
                        80 + words_settings.index(i) * 60))
                    screen.blit(pygame.transform.scale(red_soul, (20, 20)), (x_soul_menu,
                        y_soul_menu))
        if sec == -22:
            for i in range(len(words_achievements)):
                for j in range(len(words_achievements[i])):
                    itog = words_achievements[i][j]
                    color_text = "white"
                    if "1" in words_achievements[i][j]:
                        itog = words_achievements[i][j].replace("1", "")
                        color_text = "yellow"
                    if itog in (all_txts[23], ""):
                        itog = f7.render(itog, True, Color(color_text))
                    else:
                        itog = ach_hide
                        if color_text == "yellow":
                            itog = ach_hide_yel
                    screen.blit(itog, (20 + j * 100, 100 + i * 100))
                    pygame.draw.rect(screen, Color("black"), (400, 0, 200, 600))
                    pygame.draw.rect(screen, Color("white"), (400, 0, 200, 600), 3)
                    txt_ach = ""
                    if words_achievements[1][0] == "first1":
                        txt_ach = all_txts[10]
                    if words_achievements[1][1] == "second1":
                        txt_ach = all_txts[11]
                    if words_achievements[1][2] == "third1":
                        txt_ach = all_txts[12]
                    if words_achievements[1][3] == "fourth1":
                        txt_ach = all_txts[13]
                    if words_achievements[2][0] == "fifth1":
                        txt_ach = all_txts[14]
                    if words_achievements[2][1] == "sixth1":
                        txt_ach = all_txts[15]
                    if words_achievements[2][2] == "seventh1":
                        txt_ach = all_txts[16]
                    if words_achievements[2][3] == "eighth1":
                        txt_ach = all_txts[17]


                    if "/" in txt_ach:
                        txt_ach = txt_ach.split("/")
                    y_word = 0
                    for l in txt_ach:
                        y_w = 70 + txt_ach.index(l) * 30
                        if txt_ach.index(l) == 0:
                            if "2" in l:
                                f = l.replace("2", "")
                                f = f.split("'")
                                txt_i = f7.render(f[0], True, Color("white"))
                                screen.blit(txt_i, (410, 10))
                                txt_i = f7.render(f[1], True, Color("white"))
                                screen.blit(txt_i, (410, 40))
                                continue
                            y_w = 40
                        txt_i = f7.render(l, True, Color("white"))
                        pygame.draw.line(screen, Color("white"), (400, 70), (600, 70), 3)
                        screen.blit(txt_i, (410, y_w))

        if sec == -23:
            word_ex = words_extras[0][0].replace("1", "")
            word_ex = f7.render(word_ex, True, Color("yellow"))
            screen.blit(word_ex, (50, 80))
            word_ex = f7.render(all_txts[18], True, Color("pink"))
            screen.blit(word_ex, (270, 300))

        if sec == -1000:
            f = pygame.font.Font("resours/determ.otf", 80)
            end = f.render("DEMO END!", True, Color("white"))
            data.screen.fill("black")
            data.screen.blit(end, (140, 250))
            print("1")

        screen_x2 = Surface((600, 600))
        screen_x2.blit(screen, (0, 0))

        change_menu(screen_x1, screen_x2)


        ### EXIT ###
        if quit_timer != -1:
            quit_timer += 1
            if quit_timer <= 15:
                exiting_t = all_txts[19]
            if 15 < quit_timer <= 30:
                exiting_t = all_txts[20]
            if 30 < quit_timer <= 45:
                exiting_t = all_txts[21]
            if 45 < quit_timer <= 60:
                exiting_t = all_txts[22]
            if language == "ru":
                ex = f5.render(exiting_t, False, Color("white"))
            else:
                ex = f1.render(exiting_t, False, Color("white"))
            ex.set_alpha(quit_timer * 20)
            screen.blit(ex, (10, 10))
        if quit_timer == 60:
            run = False
        ###------###
        if scr == "full":
            screen2 = pygame.transform.scale(screen, (monitorsize[1], monitorsize[1]))
            screen1.blit(screen2, (((monitorsize[0] - monitorsize[1]) // 2, 0)))
        if scr == "small":
            screen1.blit(screen, (0, 0))

        pygame.display.flip()

pygame.quit()
sys.exit()
