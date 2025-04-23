import setting
from show import show
from random import randint
from pygame import transform


def make_pipes():

    setting.pipe_pos_y = randint(350, 500)
    setting.pipe_1 = [setting.pipe_img, setting.pipe_pos_y]
    setting.pipe_2 = [
        transform.flip(setting.pipe_img, flip_x=False, flip_y=True),
        setting.pipe_pos_y - 1000,
    ]


def move_pipe():

    setting.pipe_pos_x -= 2.5
