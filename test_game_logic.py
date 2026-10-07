import unittest

from game_logic import Facing, InputState, PlayerState, axis, movement, step_player


class AxisTests(unittest.TestCase):
    def test_single_key_sets_axis_direction(self):
        self.assertEqual(axis(True, False), -1)
        self.assertEqual(axis(False, True), 1)

    def test_opposing_keys_cancel(self):
        self.assertEqual(axis(True, True), 0)
        self.assertEqual(axis(False, False), 0)


class MovementTests(unittest.TestCase):
    def test_all_four_directions_are_supported(self):
        self.assertEqual(movement(InputState(left=True)), (-1, 0))
        self.assertEqual(movement(InputState(right=True)), (1, 0))
        self.assertEqual(movement(InputState(up=True)), (0, 1))
        self.assertEqual(movement(InputState(down=True)), (0, -1))

    def test_vertical_movement_keeps_previous_facing(self):
        left = PlayerState(640, 512, Facing.LEFT)
        self.assertEqual(step_player(left, InputState(up=True)).facing, Facing.LEFT)
        self.assertEqual(step_player(left, InputState(down=True)).facing, Facing.LEFT)

    def test_horizontal_movement_changes_facing(self):
        player = PlayerState(640, 512, Facing.RIGHT)
        self.assertEqual(step_player(player, InputState(left=True)).facing, Facing.LEFT)

    def test_player_stops_at_every_screen_edge(self):
        player = PlayerState(50, 50)
        bottom_left = step_player(player, InputState(left=True, down=True))
        self.assertEqual((bottom_left.x, bottom_left.y), (50, 50))

        player = PlayerState(1230, 974)
        top_right = step_player(player, InputState(right=True, up=True))
        self.assertEqual((top_right.x, top_right.y), (1230, 974))


if __name__ == "__main__":
    unittest.main()
