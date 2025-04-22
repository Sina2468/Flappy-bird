import pygame
import setting
import setup_screen
from show import show
from bird_gravity import bird_gravity, bird_gravity_no


pygame.init()

setup_screen.setup_screen()


def shows():
    show(setting.bg_img, (0, 0))
    show(setting.bird_img, setting.bird_pos)


while setting.running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False

    #     if event.type == pygame.KEYDOWN:

    #         if event.key == pygame.K_SPACE:
    #             bird_gravity_no()

    # bird_gravity()
    shows()

    pygame.display.update()


pygame.quit()
