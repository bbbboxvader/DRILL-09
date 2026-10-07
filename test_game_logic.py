import unittest

from game_logic import axis


class AxisTests(unittest.TestCase):
    def test_single_key_sets_axis_direction(self):
        self.assertEqual(axis(True, False), -1)
        self.assertEqual(axis(False, True), 1)

    def test_opposing_keys_cancel(self):
        self.assertEqual(axis(True, True), 0)
        self.assertEqual(axis(False, False), 0)


if __name__ == "__main__":
    unittest.main()
