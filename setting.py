from pygame import image, transform


screen_size = (500, 800)

icon = image.load("assets\\img\\game_icon.png")

bg_img = image.load("assets\\img\\bg1.png")
bg_img = transform.scale(bg_img, screen_size)

bird_img = image.load("assets\\img\\red_bird_up_flap.png")
bird_img = transform.scale(bird_img, (60, 50))
bird_pos = (80, 350)


game_name = "Flappy bird"


running = True
