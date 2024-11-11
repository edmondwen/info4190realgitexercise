import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate(5, 5, "+"), 10)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(50, 15, "-"), 35)

    def test_multiply(self):
        self.assertEqual(calculator.calculate(3, 3, "*"), 9)

    def test_divide(self):
        self.assertEqual(calculator.calculate(100, 10, "/"), 10)
#comment for test calculator

if __name__ == "__main__":
    unittest.main()