"""화면과 독립적으로 테스트할 수 있는 캐릭터 이동 규칙."""

from dataclasses import dataclass
from enum import Enum

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
SPRITE_SIZE = 100
FRAME_COUNT = 8
MOVE_SPEED = 5


class Facing(Enum):
    LEFT = -1
    RIGHT = 1


@dataclass
class InputState:
    left: bool = False
    right: bool = False
    up: bool = False
    down: bool = False


@dataclass(frozen=True)
class PlayerState:
    x: float
    y: float
    facing: Facing = Facing.RIGHT


def axis(negative: bool, positive: bool) -> int:
    """서로 반대인 두 키 상태를 -1, 0, 1 축 값으로 바꾼다."""
    return int(positive) - int(negative)


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def movement(keys: InputState) -> tuple[int, int]:
    return axis(keys.left, keys.right), axis(keys.down, keys.up)


def step_player(
    player: PlayerState,
    keys: InputState,
    speed: float = MOVE_SPEED,
    width: int = CANVAS_WIDTH,
    height: int = CANVAS_HEIGHT,
) -> PlayerState:
    dx, dy = movement(keys)
    half = SPRITE_SIZE / 2
    facing = player.facing
    if dx < 0:
        facing = Facing.LEFT
    elif dx > 0:
        facing = Facing.RIGHT
    return PlayerState(
        clamp(player.x + dx * speed, half, width - half),
        clamp(player.y + dy * speed, half, height - half),
        facing,
    )

