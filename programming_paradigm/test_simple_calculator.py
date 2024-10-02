import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test positive and negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test adding zero
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtraction(self):
        """Test the subtract method."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test positive and negative
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        # Test subtracting zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        """Test the multiply method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test positive and negative
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test multiplying by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4.0), 10.0)

    def test_division(self):
        """Test the divide method."""
        # Test positive numbers
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, -3), 2)
        # Test positive and negative
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test zero divided by a number
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)
        # Test division resulting in a floating point number
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_operations_with_large_numbers(self):
        """Test operations with very large numbers."""
        large_num1 = 1e100
        large_num2 = 1e100
        self.assertEqual(self.calc.add(large_num1, large_num2), 2e100)
        self.assertEqual(self.calc.subtract(large_num1, large_num2), 0)
        self.assertEqual(self.calc.multiply(large_num1, large_num2), 1e200)
        self.assertEqual(self.calc.divide(large_num1, large_num2), 1)

    def test_operations_with_small_numbers(self):
        """Test operations with very small numbers."""
        small_num1 = 1e-100
        small_num2 = 1e-100
        self.assertEqual(self.calc.add(small_num1, small_num2), 2e-100)
        self.assertEqual(self.calc.subtract(small_num1, small_num2), 0)
        self.assertEqual(self.calc.multiply(small_num1, small_num2), 0)
        self.assertEqual(self.calc.divide(small_num1, small_num2), 1)

if __name__ == '__main__':
    unittest.main()
