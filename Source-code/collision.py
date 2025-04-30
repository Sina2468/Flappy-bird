import setting
from time import sleep


def check_collision():
    if setting.bird_img_rect.colliderect(
        setting.pipe_img_rect
    ) or setting.bird_img_rect.colliderect(setting.pipe_img_rect_2):
        setting.game_over_sound.play()
        sleep(3)
        setting.start = False

        if setting.score > setting.high_score:
            setting.high_score = setting.score
