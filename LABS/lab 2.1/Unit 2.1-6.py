import unittest
from functools import cmp_to_key

def comp(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

class TestSolve(unittest.TestCase):
    def test_solve(self):
        n = 5
        a = [4, 3, 2, 1, 0]
        expected = '01234'

        result = solve(a)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
