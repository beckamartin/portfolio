import unittest
from solution import find_it


class TestFindIt(unittest.TestCase):
    def test_find_it_1(self):
        self.assertEqual(find_it([7]), 7)

    def test_find_it_2(self):
        self.assertEqual(find_it([1,1,2]), 2)

    def test_find_it_3(self):
        self.assertEqual(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]), 4)
    

if __name__ == '__main__':
    unittest.main()