import unittest
from solution import array_diff


class TestArrayDiff(unittest.TestCase):
    def test_array_diff_1(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])

    def test_array_diff_2(self):
        self.assertEqual(array_diff([1, 2, 2, 2, 3], [2]), [1, 3])

        
if __name__ == '__main__':
    unittest.main()