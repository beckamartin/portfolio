import unittest
from solution import shortcut


class TestShortcut(unittest.TestCase):
    def test_shortcut(self):
        self.assertEqual(shortcut("hello"), "hll")
        self.assertEqual(shortcut("codewars"), "cdwrs")
        self.assertEqual(shortcut("goodbye"), "gdby")
        self.assertEqual(shortcut("HELLO"), "HELLO")


if __name__ == '__main__':
    unittest.main()