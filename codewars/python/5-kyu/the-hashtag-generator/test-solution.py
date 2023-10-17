import unittest
from solution import generate_hashtag


class TestGenerateHashtag(unittest.TestCase):
    def test_generate_hashtag_1(self):
        self.assertEqual(generate_hashtag(" Hello there thanks for trying my Kata"), "#HelloThereThanksForTryingMyKata")

    def test_generate_hashtag_2(self):
        self.assertEqual(generate_hashtag("    Hello     World   "), "#HelloWorld")

    def test_generate_hashtag_3(self):
        self.assertEqual(generate_hashtag(""), False)


if __name__ == '__main__':
    unittest.main()