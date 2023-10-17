import unittest
from solution import snail


class TestSnail(unittest.TestCase):
    def test_snail_1(self):
        self.assertEqual(snail([[1,2,3], [8,9,4], [7,6,5]]), [1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
    unittest.main()