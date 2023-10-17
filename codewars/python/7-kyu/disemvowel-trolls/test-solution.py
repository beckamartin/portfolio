import unittest
from solution import disemvowel


class TestDisemvowel(unittest.TestCase):
    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

        
if __name__ == '__main__':
    unittest.main()