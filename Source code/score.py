import setting
from show import show


def display_score():
    game_score = setting.game_font.render(
        f"SCORE : {setting.score}", False, (255, 255, 255), None
    )

    game_high_score = setting.game_font.render(
        f"H-SCORE : {setting.high_score}", False, (255, 255, 255), None
    )

    if setting.start:

        show(game_score, (150, 50))

    if setting.start == False:
        show(game_score, (30, 220))
        show(game_high_score, (250, 220))


def save_score():
    with open("save.txt", "w") as save_file:
        save_file.write(str(setting.high_score))
