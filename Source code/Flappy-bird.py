import pygame
import setting
import setup_screen
from show import show, show_pipe
from bird_gravity import bird_gravity
from moving import move_pipe, move_floor
from default import default
from collision import check_collision
from score import display_score, save_score


pygame.init()

setup_screen.setup_screen()


def shows_game():
    show(setting.bg_img, setting.bg_pos)
    show_pipe()
    show(setting.floor_img, (setting.floor_pos_x, setting.floor_pos_y))
    show(setting.floor_img, (setting.floor_pos_x + 500, setting.floor_pos_y))
    show(setting.bird_img, setting.bird_img_rect)


def show_start():
    show(setting.bg_img, setting.bg_pos)
    show(setting.start_img, setting.start_pos)


while setting.running:

    if setting.start:

        shows_game()
        bird_gravity()
        move_pipe()
        move_floor()
        check_collision()
        display_score()
        save_score()

    else:
        show_start()
        display_score()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                setting.move = -5

            if event.key == pygame.K_r:
                setting.start = True
                default()


pygame.quit()
