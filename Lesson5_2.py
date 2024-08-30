# creating a modified calculator that will work until the user decides to stop it
# v1 - if-else version
while True:
    # getting nums and operand first
    num1 = float(input("Give me a number: "))
    operation = input("Pick an operand e.g. (+, -, *, /): ")
    num2 = float(input("Give me a second number: "))

    # here goes if, elif, else solution
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error, we cannot divide by 0!"
    else:
        result = "Invalid value"

    print("Result:", result)

    # asking user if he/she wants to continue
    continue_calculation = input("Do you want to perform another calculation? (yes or y to continue): ")
    if continue_calculation.lower() not in ["yes", "y"]:
        print("Exiting the calculator. Goodbye!")
        break

# v2 match version

while True:
    # getting nums and operand first
    num1 = float(input("Give me a number: "))
    operation = input("Pick an operand e.g. (+, -, *, /): ")
    num2 = float(input("Give me a second number: "))

    # here goes match instead if, etc.
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error, we cannot divide by 0!"
        case _:
            result = "Invalid value"

    print("Result:", result)

    # asking user if he/she wants to continue
    continue_calculation = input("Do you want to perform another calculation? (yes or y to continue): ")
    if continue_calculation.lower() not in ["yes", "y"]:
        print("Exiting the calculator. Goodbye!")
        break