from pico2d import *


open_canvas()
map = load_image('TUK_GROUND.png')
character = load_image('character1.png')

def handle_events():
    global running, dir_x, dir_y
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                clear_canvas()
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

# def right_move():
#     clear_canvas()
#     character.clip_draw()
#
# def left_move():
#     clear_canvas()
#     character.clip_composite_draw()

# def render():
#     global frame


running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
# fill here
while running:
    clear_canvas()
    map.draw(800 // 2, 600 // 3)
    character.clip_draw(frame*100, 400, 100, 100, x, y)
    handle_events()
    update_canvas()
    frame = (frame + 1) % 6
    x += dir_x * 5
    y += dir_y * 5
    delay(0.03)

close_canvas()

