import argparse
import logging
import sys

from calculator_logic import add, subtract, multiply, divide

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def parse_numeric_input(value):
    """Convert an input string to a number and raise ValueError on failure."""
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"Invalid number: {value!r}. Please enter a valid integer.") from exc


def evaluate_expression(num1, op, num2):
    """Evaluate the arithmetic expression using the existing function names."""
    if op == "+":
        return add(num1, num2)
    if op == "-":
        return subtract(num1, num2)
    if op == "*":
        return multiply(num1, num2)
    if op == "/":
        return divide(num1, num2)
    raise ValueError(f"Invalid operator: {op!r}. Supported operators: +, -, *, /")


def run_interactive_mode():
    """Run the original interactive prompt mode if no CLI arguments are provided."""
    try:
        num1 = parse_numeric_input(input("enter first number->"))
        op = input("enter operator (+, -, *, /)->")
        num2 = parse_numeric_input(input("enter second number->"))
    except ValueError as exc:
        logging.error(str(exc))
        return 1

    try:
        result = evaluate_expression(num1, op, num2)
    except ValueError as exc:
        logging.error(str(exc))
        return 1
    except ZeroDivisionError as exc:
        logging.error(f"Calculation error: {exc}")
        return 1

    print("Result:", result)
    return 0


def build_parser():
    """Create the argparse parser with usage instructions and help text."""
    parser = argparse.ArgumentParser(
        description="CLI calculator supporting +, -, *, and / operations.",
        epilog="Examples: python3 cli.py 10 + 5   python3 cli.py 9 / 3",
    )
    parser.add_argument("num1", nargs="?", help="First number")
    parser.add_argument("op", nargs="?", choices=["+", "-", "*", "/"], help="Operator")
    parser.add_argument("num2", nargs="?", help="Second number")
    return parser


def main(argv=None):
    """Entry point for the CLI. Supports non-interactive and interactive usage."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.num1 is None and args.op is None and args.num2 is None:
        return run_interactive_mode()

    if args.num1 is None or args.op is None or args.num2 is None:
        parser.error("All three arguments (number, operator, number) are required for non-interactive mode.")

    try:
        num1 = parse_numeric_input(args.num1)
        num2 = parse_numeric_input(args.num2)
        result = evaluate_expression(num1, args.op, num2)
    except ValueError as exc:
        logging.error(str(exc))
        return 1
    except ZeroDivisionError as exc:
        logging.error(f"Calculation error: {exc}")
        return 1

    print("Result:", result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
