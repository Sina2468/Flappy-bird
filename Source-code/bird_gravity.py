import setting
from time import sleep


def bird_gravity():

    bird_rect = list(setting.bird_img_rect.topleft)

    if bird_rect[1] < 620 and bird_rect[1] > -10:
        bird_rect[1] += setting.move
        setting.move += setting.gravity

    if bird_rect[1] >= 620 or bird_rect[1] <= -10:
        setting.game_over_sound.play()
        sleep(3)
        setting.start = False
        if setting.score > setting.high_score:
            setting.high_score = setting.score

    setting.bird_img_rect.topleft = tuple(bird_rect)
