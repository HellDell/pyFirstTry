# a simple calculator w/ such operands as (+, -, *, /)

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
    result = "Invalid value" # # will not reach this part of the code because
        # the float cannot process a "." or "a" and will output an error

print("Result:", result)

# same shit but w/ match

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
        result = "Invalid value"  # will not reach this part of the code because
        # the float cannot process a "." or "a" and will output an error

print("Result: ", result)
