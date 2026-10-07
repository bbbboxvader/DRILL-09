from pico2d import *

from game_logic import CANVAS_HEIGHT, CANVAS_WIDTH, InputState, PlayerState


def run():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = load_image("TUK_GROUND.png")
    character = load_image("animation_sheet.png")
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()
    close_canvas()


if __name__ == "__main__":
    run()
