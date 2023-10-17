import unittest
from solution import strip_comments


class TestStripComments(unittest.TestCase):
    def test_strip_comments_1(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
        
    def test_strip_comments_2(self):
        self.assertEqual(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

    def test_strip_comments_3(self):
        self.assertEqual(strip_comments(" a #b\nc\nd $e f g", ["#", "$"]), " a\nc\nd")


if __name__ == "__main__":
    unittest.main()