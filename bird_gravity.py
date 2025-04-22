import setting


def bird_gravity():
    bird_pos_list = list(setting.bird_pos)
    bird_pos_list[1] += 3.5
    setting.bird_pos = bird_pos_list


def bird_gravity_no():
    bird_pos_list = list(setting.bird_pos)
    bird_pos_list[1] -= 3.5
    setting.bird_pos = bird_pos_list
