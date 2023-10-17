import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(solution("abc", "bc"), True)

    def test_solution_2(self):
        self.assertEqual(solution("abc", "d"), False)

        
if __name__ == '__main__':
    unittest.main()