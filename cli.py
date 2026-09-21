from calculator_logic import add, subtract, multiply, divide

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("Result:", result)
    except ValueError:
        print("Please enter valid numbers.")

    again = input("Calculate again? (y/n): ")
    if again != "y":
        break