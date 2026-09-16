"""Calculator logic for a simple arithmetic CLI application."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference between a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b equals 0.
    """
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b