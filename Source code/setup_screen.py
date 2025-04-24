from pygame import display
import setting


screen = display.set_mode(setting.screen_size)

def setup_screen():

    display.set_caption(setting.game_name)
    display.set_icon(setting.icon)
