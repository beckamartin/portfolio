import unittest
from solution import count_smileys


class TestCountSmileys(unittest.TestCase):
    def test_count_smileys_1(self):
        self.assertEqual(count_smileys([':)', ';(', ';}', ':-D']), 2)

    def test_count_smileys_2(self):
        self.assertEqual(count_smileys([';D', ':-(', ':-)', ';~)']), 3)
    
    def test_count_smileys_3(self):
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
        

if __name__ == '__main__':
    unittest.main()