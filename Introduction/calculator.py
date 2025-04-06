def calculator():
    print("Simple Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

    # Take user input
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform the operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator! Please use +, -, *, or /")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers.")

# Run the calculator
calculator()
