import unittest
from solution import compute_depth


class TestComputeDepth(unittest.TestCase):
    def test_compute_depth_1(self):
        self.assertEqual(compute_depth(1), 10)

    def test_compute_depth_2(self):
        self.assertEqual(compute_depth(42), 9)


if __name__ == "__main__":
    unittest.main()