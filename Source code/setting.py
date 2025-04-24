from pygame import image, transform, mixer, font

mixer.init()
font.init()

screen_size = (500, 800)

icon = image.load("assets\\img\\game_icon.png")

game_name = "Flappy bird"

bg_img = image.load("assets\\img\\bg1.png")
bg_img = transform.scale(bg_img, screen_size)
bg_pos = (0, 0)

bird_img = image.load("assets\\img\\red_bird_up_flap.png")
bird_img = transform.scale(bird_img, (60, 50))
bird_pos_x = 80
bird_pos_y = 350
bird_img_rect = bird_img.get_rect(topleft=(bird_pos_x, bird_pos_y))

floor_img = image.load("assets\\img\\floor.png")
floor_img = transform.scale(floor_img, (500, 150))
floor_pos_x = 0
floor_pos_y = 650

pipe_img = image.load("assets\\img\\pipe_green.png")
pipe_img = transform.scale(pipe_img, (80, 800))
pipe_pos_x = 500
pipe_pos_y = 350
pipe_img_rect = pipe_img.get_rect(topleft=(pipe_pos_x, pipe_pos_y))
pipe_img_rect_2 = pipe_img.get_rect(topleft=(pipe_pos_x, pipe_pos_y - 1050))


start_img = image.load("assets\\img\\message.png")
start_img = transform.scale(start_img, (400, 700))
start_pos = (50, 50)

game_over_sound = mixer.Sound("assets\\sound\\smb_mario_die.wav")

pipe_sound = mixer.Sound("assets\\sound\\smb_stomp.wav")

game_font = font.Font("assets\\font\\Flappy.TTF", 40)


running = True
start = False

gravity = 0.1
move = 0

score = 0
try:
    with open("save.txt", "x+") as save_file:
        high_score = save_file.read()

        if high_score == "":
            high_score = 0

        else:
            high_score = int(high_score)

except:
    with open("save.txt", "r+") as save_file:
        high_score = save_file.read()

        if high_score == "":
            high_score = 0

        else:
            high_score = int(high_score)
