from setup_screen import screen
import setting
from pygame import transform
from random import randint


def show(image, pos):
    screen.blit(image, pos)


def show_pipe():

    pipe_rect = list(setting.pipe_img_rect.topleft)

    if pipe_rect[0] >= -80:
        show(setting.pipe_img, setting.pipe_img_rect)
        show(
            transform.flip(setting.pipe_img, False, True),
            setting.pipe_img_rect_2,
        )
    if pipe_rect[0] < -80:
        pipe_rect[0] = 500
        pipe_rect[1] = randint(300, 500)

    if pipe_rect[0] == 80:
        setting.score += 1
        setting.pipe_sound.play()

    setting.pipe_img_rect.topleft = tuple(pipe_rect)
    setting.pipe_img_rect_2.topleft = (pipe_rect[0], pipe_rect[1] - 1050)
