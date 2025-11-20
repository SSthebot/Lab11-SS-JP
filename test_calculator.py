# https://github.com/SSthebot/Lab11-SS-JP
# Partner 1: Shyaam Shanmugam
# Partner 2: Julian Perez

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-2, 3), 1)
        self.assertEqual(calculator.add(-2, -3), -5)
        self.assertEqual(calculator.add(0, 5), 5)
        self.assertAlmostEqual(calculator.add(2.5, 3.7), 6.2)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)
        self.assertEqual(calculator.subtract(-2, 3), -5)
        self.assertEqual(calculator.subtract(-2, -3), 1)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertAlmostEqual(calculator.subtract(5.5, 2.3), 3.2)
    
    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, -5)
    
    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(2, 16), 4.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.logarithm(3, 27), 3.0)
        self.assertAlmostEqual(calculator.logarithm(2, 1), 0.0)
    
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-5, 100)


    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 3), -6)
        self.assertEqual(calculator.mul(-2, -3), 6)
        self.assertEqual(calculator.mul(0, 5), 0)
        self.assertEqual(calculator.mul(5, 0), 0)
        self.assertAlmostEqual(calculator.mul(2.5, 4), 10.0)


    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5.0)
        self.assertEqual(calculator.div(4, 20), 5.0)
        self.assertAlmostEqual(calculator.div(3, 10), 3.333333333, places=7)
        self.assertEqual(calculator.div(-2, 10), -5.0)
        self.assertEqual(calculator.div(2, -10), -5.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)


    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)


    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.4142135623730951, places=7)
        self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 0), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(2.5, 6.0), 6.5)


    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        self.assertAlmostEqual(calculator.square_root(2), 1.4142135623730951, places=7)
        self.assertAlmostEqual(calculator.square_root(0.25), 0.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


if __name__ == '__main__':
    unittest.main()