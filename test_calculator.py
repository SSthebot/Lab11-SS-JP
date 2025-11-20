# https://github.com/SSthebot/Lab11-SS-JP
# Partner 1: Shyaam Shanmugam
# Partner 2: Julian Perez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 10), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 20), -10)
        self.assertEqual(subtract(0, 7), -7)



    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)



    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == '__main__':
    unittest.main()