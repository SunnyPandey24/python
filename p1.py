# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

print("Simple Calculator")
print("Select operation: +, -, *, /")

while True:
    choice = input("Enter operation (+ - * / or 'q' to quit): ")

    if choice == 'q':
        print("Exiting Calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"Result: {add(num1, num2)}")
    elif choice == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Input")
