from calculator_logic import add, subtract, multiply, divide

num1 = float(input("enter first number->"))
op = input("enter operator (+, -, *, /)->")
num2 = float(input("enter second number->"))

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
