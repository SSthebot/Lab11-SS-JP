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
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, -5)
    
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
    
   


if __name__ == '__main__':
    unittest.main()