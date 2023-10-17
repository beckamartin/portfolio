import unittest
from solution import find_uniq


class TestFindUniq(unittest.TestCase):
    def test_find_uniq_1(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)

    def test_find_uniq_2(self):
        self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
    

if __name__ == '__main__':
    unittest.main()