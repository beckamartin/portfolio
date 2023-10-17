import unittest
from solution import transpose


class TestTranspose(unittest.TestCase):
    def test_transpose_1(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
    

if __name__ == '__main__':
    unittest.main()