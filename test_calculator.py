import unittest

from calculator_logic import add, subtract, multiply, divide
from cli import evaluate_expression, parse_numeric_input


class CalculatorLogicTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(9, 4), 5)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)

    def test_evaluate_expression_valid(self):
        self.assertEqual(evaluate_expression(10, "+", 5), 15)
        self.assertEqual(evaluate_expression(10, "-", 5), 5)
        self.assertEqual(evaluate_expression(10, "*", 5), 50)
        self.assertEqual(evaluate_expression(10, "/", 5), 2)

    def test_evaluate_expression_invalid_operator(self):
        with self.assertRaises(ValueError):
            evaluate_expression(10, "?", 5)

    def test_parse_numeric_input_invalid(self):
        with self.assertRaises(ValueError):
            parse_numeric_input("abc")


if __name__ == "__main__":
    unittest.main()
