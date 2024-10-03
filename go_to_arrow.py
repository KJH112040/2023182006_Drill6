from pico2d import*
import random

open_canvas()

tuk = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global run
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            run = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                run = False

def random_move_arrow():
    global arrow_x, arrow_y, goal
    arrow_x, arrow_y = random.randrange(50,750),random.randrange(52,548)
    goal = False

run = True
frame_x = 0
dir = 3

random_move_arrow()

while run:
    clear_canvas()
    tuk.draw(400,300,800,600)
    boy.clip_draw(frame_x*802//8,dir*402//4,802//8,402//4,400,300,90,90)
    arrow.draw(arrow_x,arrow_y,50,52)
    update_canvas()
    handle_events()
    if goal:
        random_move_arrow()
    else:
        a=0
        
    delay(0.05)

close_canvas()
