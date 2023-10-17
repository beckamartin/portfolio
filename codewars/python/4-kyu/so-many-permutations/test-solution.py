import unittest
from solution import permutations


class TestPermutations(unittest.TestCase):
    def test_permutatioins_1(self):
        self.assertEqual(permutations("a"), ["a"])

    def test_permutatioins_2(self):
        self.assertEqual(permutations("ab"), ["ab", "ba"])
    
    def test_permutatioins_3(self):
        self.assertEqual(permutations("aabb"), ["aabb", "abab", "abba", "baab", "baba", "bbaa"])


if __name__ == "__main__":
    unittest.main()