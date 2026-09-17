def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b        

num1 = int(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

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