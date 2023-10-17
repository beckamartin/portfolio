import unittest
from solution import grow


class TestGrow(unittest.TestCase):
    def test_grow(self):
        self.assertEqual(grow([1, 2, 3, 4]), 24)

        
if __name__ == '__main__':
    unittest.main()