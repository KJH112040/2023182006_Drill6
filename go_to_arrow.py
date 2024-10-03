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

def go_to_arrow(arrow_x, arrow_y):
    global boy_x, boy_y
    if arrow_x-boy_x != 0:
        a = (arrow_y-boy_y)/(arrow_x-boy_x)
        b = boy_y - boy_x * a

        if boy_x < arrow_x:
            if boy_x + 10 < arrow_x:
                boy_x += 10
            else:
                boy_x += 1
        elif boy_x > arrow_x:
            if boy_x - 10 > arrow_x:
                boy_x -= 10
            else:
                boy_x -= 1
        boy_y = int(a * boy_x + b)
    elif arrow_x-boy_x == 0:
        if boy_y < arrow_y:
            if boy_y + 3 < arrow_y:
                boy_y += 3
            else:
                boy_y += 1
        elif boy_y > arrow_y:
            if boy_y - 3 > arrow_y:
                boy_y -= 3
            else:
                boy_y -= 1
        

run = True
frame_x = 3
dir = 3
boy_x = 400
boy_y = 300

random_move_arrow()

while run:
    clear_canvas()
    tuk.draw(400,300,800,600)
    arrow.draw(arrow_x,arrow_y,50,52)
    boy.clip_draw(frame_x*802//8,dir*402//4,802//8,402//4,boy_x,boy_y,100,100)
    update_canvas()
    handle_events()
    if goal:
        random_move_arrow()
    else:
        if arrow_x == boy_x and arrow_y == boy_y:
            if dir == 0:
                dir = 2
            elif dir == 1:
                dir = 3
            frame_x = 3
            goal = True
        else:
            if arrow_x > boy_x:
                dir = 1
            elif arrow_x < boy_x:
                dir = 0
            elif arrow_x == boy_x:
                if dir == 2:
                    dir = 0
                elif dir == 3:
                    dir = 1

            go_to_arrow(arrow_x,arrow_y)
            
            frame_x = (frame_x + 1) % 8
        
    delay(0.05)

close_canvas()
