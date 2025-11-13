# calculator.py
# Solution for Elevate Labs Task 1: Build a Calculator CLI App

# 1. Define functions for each operation [cite: 8]
def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

# 3. Loop until user chooses to exit [cite: 10]
while True:
    print("\n--- Calculator Menu ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # 2. Take user input using input() [cite: 9]
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if choice is one of the options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue  # Go back to the start of the loop

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    
    elif choice == '5':
        print("Exiting calculator. Goodbye!")
        break  # Exit the while loop
    
    else:
        print("Invalid choice. Please select from 1, 2, 3, 4, or 5.")