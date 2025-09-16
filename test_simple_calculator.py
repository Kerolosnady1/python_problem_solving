# unittest on simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class testing(unittest.TestCase):
    def test_add(self):
        assert SimpleCalculator.add(self, 5, 5) == 10, "Should be 10"
        assert SimpleCalculator.add(self, -1, -1) == -2, "Should be -2"
        assert SimpleCalculator.add(self, -2, 5) == 3, "Should be 3"
        assert SimpleCalculator.add(self, 5, -2) == 3, "Should be 3"

    def test_subtract(self):
        self.assertTrue(SimpleCalculator.subtract(self, 5, 5) == 0, "Should be 0")
        self.assertTrue(SimpleCalculator.subtract(self, -1, -1) == 0, "Should be 0")
        self.assertTrue(SimpleCalculator.subtract(self, -2, 5) == -7, "Should be -7")
        self.assertTrue(SimpleCalculator.subtract(self, 5, -3) == 8, "Should be 8")

    def test_multiply(self):
        self.assertTrue(SimpleCalculator.multiply(self, 5, 5) == 25, "Should be 25")
        self.assertTrue(SimpleCalculator.multiply(self, -1, -1) == 1, "Should be 1")
        self.assertTrue(SimpleCalculator.multiply(self, -2, 5) == -10, "Should be -10")
        self.assertTrue(SimpleCalculator.multiply(self, 5, -2) == -10, "Should be -10")

    def test_divide(self):
        self.assertTrue(SimpleCalculator.divide(self, 5, 0) == None, "Should be ZeroDivisionError")
        self.assertTrue(SimpleCalculator.divide(self, 5, 5) == 1, "Should be One")
        self.assertTrue(SimpleCalculator.divide(self, -1, -1) == 1, "Should be One")
        self.assertTrue(SimpleCalculator.divide(self, -2, 5) == -0.4, "Should be -0.4")
        self.assertTrue(SimpleCalculator.divide(self, 5, -2) == -2.5, "Should be -2.5")

    


if __name__ == "__main__":
    unittest.main()

