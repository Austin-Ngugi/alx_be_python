import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), 10)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtact(-5,-5), -10)
        self.assertEqual(self.calc.subtact(-10,5), -5)
        
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-5,-5), 25)
        self.assertEqual(self.calc.multiply(5,5), 25)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(5, 1), 5)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(5, 10), 0.5)
        
if __name__ = "__main__":
    unittest.main()