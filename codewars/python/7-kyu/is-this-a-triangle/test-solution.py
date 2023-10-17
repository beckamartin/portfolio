import unittest
from solution import is_triangle


class TestIsTriangle(unittest.TestCase):
    def test_is_triangle_1(self):
        self.assertEqual(is_triangle(1, 2, 2), True)

    def test_is_triangle_2(self):
        self.assertEqual(is_triangle(7, 2, 2), False)

    def test_is_triangle_3(self):
        self.assertEqual(is_triangle(0, 2, 3), False)


if __name__ == "__main__":
    unittest.main()