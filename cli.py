def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("enter a number -> "))
op = input("select an operator (+, -, *, /) -> ")
num2 = float(input("enter another number-> "))

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

print(result)