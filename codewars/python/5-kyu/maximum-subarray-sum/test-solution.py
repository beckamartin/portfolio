import unittest
from solution import max_sequence


class TestMaxSequence(unittest.TestCase):
    def test_max_sequence_1(self):
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()