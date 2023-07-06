# This is a refactored version of the simple calculator program in Python.

# Define the functions for the four basic operations.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Get the user's input for the two numbers and the operation to perform.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation to perform (+, -, *, /): ")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    # Perform the operation and print the result.
    if operation in operations:
        result = operations[operation](num1, num2)
        print("The result is:", result)
    else:
        print("Invalid operation.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
