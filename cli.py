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
