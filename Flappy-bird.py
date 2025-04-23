import pygame
import setting
import setup_screen
from show import show, show_pipe
from bird_gravity import bird_gravity
from pipes import move_pipe


pygame.init()

setup_screen.setup_screen()


def shows():
    show(setting.bg_img, setting.bg_pos)
    show_pipe()
    show(setting.floor_img, setting.floor_pos)
    show(setting.bird_img, (setting.bird_pos_x, setting.bird_pos_y))


while setting.running:

    shows()
    bird_gravity()
    move_pipe()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                setting.move = -5


pygame.quit()
