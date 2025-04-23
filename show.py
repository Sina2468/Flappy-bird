from setup_screen import screen
import setting
from pygame import transform
from random import randint


def show(image, pos):
    screen.blit(image, pos)


def show_pipe():
    if setting.pipe_pos_x >= -80:
        show(setting.pipe_img, (setting.pipe_pos_x, setting.pipe_pos_y))
        show(
            transform.flip(setting.pipe_img, False, True),
            (setting.pipe_pos_x, setting.pipe_pos_y - 1050),
        )
    if setting.pipe_pos_x < -80:
        setting.pipe_pos_x = 500
        setting.pipe_pos_y = randint(300, 500)
