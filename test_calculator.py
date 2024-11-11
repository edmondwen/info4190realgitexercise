import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate(5, 5, "+"), 10)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(50, 15, "-"), 35)


if __name__ == "__main__":
    unittest.main()
