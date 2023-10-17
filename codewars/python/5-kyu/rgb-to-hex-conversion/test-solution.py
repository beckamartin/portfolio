import unittest
from solution import rgb


class TestRgb(unittest.TestCase):
    def test_rgb_1(self):
        self.assertEqual(rgb(0,0,0), "000000")

    def test_rgb_2(self):
        self.assertEqual(rgb(1,2,3), "010203")

    def test_rgb_3(self):
        self.assertEqual(rgb(255,255,255), "FFFFFF")
    
    def test_rgb_4(self):
        self.assertEqual(rgb(254,253,252), "FEFDFC")

    def test_rgb_5(self):
        self.assertEqual(rgb(-20,275,125), "00FF7D")


if __name__ == '__main__':
    unittest.main()