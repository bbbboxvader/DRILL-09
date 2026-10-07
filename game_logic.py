"""화면과 독립적으로 테스트할 수 있는 캐릭터 이동 규칙."""

from enum import Enum

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
SPRITE_SIZE = 100
FRAME_COUNT = 8
MOVE_SPEED = 5


class Facing(Enum):
    LEFT = -1
    RIGHT = 1

