import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(solution(9), 14)

    def test_solution_2(self):
        self.assertEqual(solution(15), 45)


if __name__ == '__main__':
    unittest.main()