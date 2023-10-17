import unittest
from solution import open_or_senior


class TestOpenOrSenior(unittest.TestCase):
    def test_open_or_senior(self):
        self.assertEqual(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]), ["Open", "Open", "Senior", "Open", "Open", "Senior"])

        
if __name__ == '__main__':
    unittest.main()