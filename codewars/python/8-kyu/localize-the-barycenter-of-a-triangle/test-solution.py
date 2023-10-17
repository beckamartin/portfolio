import unittest
from solution import bar_triang


class TestBarTriang(unittest.TestCase):
    def test_bar_triang(self):
        self.assertEqual(bar_triang([4, 6], [12, 4], [10, 10]), [8.6667, 6.6667])
        self.assertEqual(bar_triang([4, 2], [12, 2], [6, 10]), [7.3333, 4.6667])

        
if __name__ == '__main__':
    unittest.main()