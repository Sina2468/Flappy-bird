from pygame import image, transform


screen_size = (500, 800)

icon = image.load("assets\\img\\game_icon.png")

bg_img = image.load("assets\\img\\bg1.png")
bg_img = transform.scale(bg_img, screen_size)
bg_pos = (0, 0)

bird_img = image.load("assets\\img\\red_bird_up_flap.png")
bird_img = transform.scale(bird_img, (60, 50))
bird_pos_x = 80
bird_pos_y = 350

floor_img = image.load("assets\\img\\floor.png")
floor_img = transform.scale(floor_img, (500, 150))
floor_pos = (0, 650)

pipe_img = image.load("assets\\img\\pipe_green.png")
pipe_img = transform.scale(pipe_img, (80, 800))
pipe_pos_x = 500
pipe_pos_y = 350

game_name = "Flappy bird"


running = True

gravity = 0.1
move = 0

pipe_1 = []
pipe_2 = []
