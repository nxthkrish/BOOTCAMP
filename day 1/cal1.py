def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def get_user_input():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

            if operation == 'exit':
                return None, None, None
            elif operation in ('+', '-', '*', '/'):
                return num1, num2, operation
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
while True:
    num1, num2, operation = get_user_input()
    if operation is None:
        print("Calculator is exiting. Goodbye!")
        break

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print(f"Result: {num1} {operation} {num2} = {result}")