import unittest

from game_logic import InputState, axis, movement


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


if __name__ == "__main__":
    unittest.main()
