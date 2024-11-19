# Basic Calculator Program
'''
Objective:

Practice creating Python programs to perform arithmetic and string, experimenting with variables, and exploring data types.
'''
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


# Basic Calculator Program

def calculator():
    print("Welcome to the Basic Calculator!")
    print("You can perform addition (+), subtraction (-), multiplication (*), or division (/).")
    
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform the operation
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Run the calculator
calculator()


