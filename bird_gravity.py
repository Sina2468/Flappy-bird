import setting


def bird_gravity():

    if setting.bird_pos_y < 600 and setting.bird_pos_y > 0:
        setting.bird_pos_y += setting.move
        setting.move += setting.gravity

    if setting.bird_pos_y >= 600 or setting.bird_pos_y <= 0:
        setting.running = False
