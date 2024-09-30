from pico2d import *

open_canvas()
school = load_image('TUK_GROUND.png')
character = load_image('character1.png')

def handle_events():
    global running, dir_x, dir_y, flip
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            if event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            if event.key == SDLK_DOWN:
                dir_y += 1

def render():
    global frame
    update_canvas()
    frame = (frame + 1) % 6
    delay(0.04)

def check_collision():
    global x, y, dir_x, dir_y, map_x, map_y
    x += dir_x * 10
    y += dir_y * 10
    if 30 > x:
        x = 30
        map_x -= dir_x * 10 # 240?
        if map_x > 640:
            map_x = 640
    elif x > 780:
        x = 780
        map_x -= dir_x * 10
        if map_x < 160:
            map_x = 160

    if 45 > y:
        y = 45
        map_y -= dir_y * 10
        if map_y > (1024 - 512):
            map_y = (1024 - 512)

    elif y > 550:
        y = 550
        map_y -= dir_y * 10
        if map_y < 90:
            map_y = 90

def decide_frame():
    global flip, dir_x, dir_y, frame, x, y
    if dir_x > 0:
        flip = ' '
    elif dir_x < 0:
        flip = 'h'

    if dir_x != 0 or dir_y != 0:
        character.clip_composite_draw(frame * 100, 300, 100, 100, 0, flip, x, y, 100, 100)
    else:
        character.clip_composite_draw(frame * 100, 400, 100, 100, 0, flip, x, y, 100, 100)

running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
flip = ' '
map_x = 800  // 2
map_y = 600 // 2

while running:
    clear_canvas()
    school.draw(map_x, map_y)
    handle_events()
    decide_frame()
    check_collision()
    render()

close_canvas()

