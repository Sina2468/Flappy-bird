import setting


def move_pipe():

    # setting.pipe_pos_x -= 2.5
    pipe_rect = list(setting.pipe_img_rect.topleft)
    pipe_rect[0] -= 2.5
    setting.pipe_img_rect.topleft = tuple(pipe_rect)

    pipe_rect_2 = list(setting.pipe_img_rect_2.topleft)
    pipe_rect_2[0] -= 3
    setting.pipe_img_rect_2.topleft = tuple(pipe_rect_2)


def move_floor():
    if setting.floor_pos_x > -500:
        setting.floor_pos_x -= 2.5
    if setting.floor_pos_x <= -500:
        setting.floor_pos_x = 0
