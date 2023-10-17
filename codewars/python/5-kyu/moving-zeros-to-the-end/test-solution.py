import unittest
from solution import move_zeros


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros_1(self):
        self.assertEqual(move_zeros([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])


if __name__ == '__main__':
    unittest.main()