# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import pygame


def change_scale(image, f1=1, f2=1):
    size = image.get_size()
    bigger_img = pygame.transform.scale(image, (int(size[0] * 2 // f1),
        int(size[1] * 2 // f2))).convert()
    return bigger_img


def rot(image, angle, track=False, cor=None):
    center = image.get_rect().center
    if track:
        center = (cor[0], cor[1] + 400)
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = center)
    return rotated_image, (new_rect[0], new_rect[1])


def shaker(power, image):
    x, y = image.get_rect()[0], image.get_rect()[1]
    return [x + 2 * power, y + 2 * power, x - 2 * power, y - 2 * power,
        x + 2 * power, y - 2 * power, x + 1 * power, y + 1 * power, x, y]
