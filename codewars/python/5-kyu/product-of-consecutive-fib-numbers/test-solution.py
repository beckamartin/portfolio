import unittest
from solution import productFib


class TestProductFib(unittest.TestCase):
    def test_product_fib_1(self):
        self.assertEqual(productFib(714), [21, 34, True])

    def test_product_fib_2(self):
        self.assertEqual(productFib(800), [34, 55, False])


if __name__ == '__main__':
    unittest.main()