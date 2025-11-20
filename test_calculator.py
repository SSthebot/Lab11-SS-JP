import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(-2, -3), 6)
        self.assertEqual(calculator.multiply(0, 5), 0)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertAlmostEqual(calculator.multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5.0)
        self.assertEqual(calculator.divide(4, 20), 5.0)
        self.assertAlmostEqual(calculator.divide(3, 10), 3.333333333, places=7)
        self.assertEqual(calculator.divide(-2, 10), -5.0)
        self.assertEqual(calculator.divide(2, -10), -5.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

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