from pico2d import *


open_canvas()
map = load_image('TUK_GROUND.png')
character = load_image('character1.png')

def handle_events():
    global running, dir_x, dir_y, idle, flip
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                flip = ' '
                idle = 300
                dir_x += 1
            elif event.key == SDLK_LEFT:
                flip = 'h'
                idle = 300
                dir_x -= 1
            elif event.key == SDLK_UP:
                idle = 300
                dir_y += 1
            elif event.key == SDLK_DOWN:
                idle = 300
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            idle = 400
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            if event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            if event.key == SDLK_DOWN:
                dir_y += 1

def right_move():
    character.clip_draw(frame*100, 300, 100, 100, x, y)

#
# def left_move():
#     clear_canvas()
#     character.clip_composite_draw()

def render():
    global frame
    update_canvas()
    frame = (frame + 1) % 6

def check_collision():
    global x, y, dir_x, dir_y
    x += dir_x * 5
    y += dir_y * 5
    if 30 > x:
        x = 30
    elif x > 780:
        x = 780

    if 45 > y:
        y = 45
    elif y > 550:
        y = 550


running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
idle = 400
flip = ' '
# fill here
while running:
    clear_canvas()
    map.draw(800 // 2, 600 // 3)
    character.clip_composite_draw(frame * 100, idle, 100, 100, 0, flip, x, y, 100, 100)
    handle_events()
    render()
    check_collision()

    delay(0.03)

close_canvas()

