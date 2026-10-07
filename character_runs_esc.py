from pico2d import *

from game_logic import (
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    SPRITE_SIZE,
    InputState,
    PlayerState,
    is_moving,
    next_frame,
    sprite_row,
    step_player,
)


def handle_events(keys: InputState) -> bool:
    running = True
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                keys.left = True
            elif event.key == SDLK_RIGHT:
                keys.right = True
            elif event.key == SDLK_UP:
                keys.up = True
            elif event.key == SDLK_DOWN:
                keys.down = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                keys.left = False
            elif event.key == SDLK_RIGHT:
                keys.right = False
            elif event.key == SDLK_UP:
                keys.up = False
            elif event.key == SDLK_DOWN:
                keys.down = False
    return running


def run():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        background = load_image("TUK_GROUND.png")
        character = load_image("animation_sheet.png")
        keys = InputState()
        player = PlayerState(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        frame = 0
        running = True
        while running:
            running = handle_events(keys)
            player = step_player(player, keys)
            clear_canvas()
            background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            row = sprite_row(player.facing, is_moving(keys))
            character.clip_draw(
                frame * SPRITE_SIZE,
                row * SPRITE_SIZE,
                SPRITE_SIZE,
                SPRITE_SIZE,
                player.x,
                player.y,
            )
            update_canvas()
            frame = next_frame(frame)
            delay(0.05)
    finally:
        close_canvas()


if __name__ == "__main__":
    run()
