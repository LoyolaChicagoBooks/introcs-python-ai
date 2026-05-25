# A simple calculator using user input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
