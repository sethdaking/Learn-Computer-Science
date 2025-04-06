def factorial(num):
    if num < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1  # Initialize result
        for i in range(1, num + 1):
            result *= i  # Multiply result by each number from 1 to num
        return result  # Return final factorial value

# Get user input
num = input("Enter a number: ")

# Convert input to integer
try:
    num = int(num)  # Corrected conversion
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter an integer.")
