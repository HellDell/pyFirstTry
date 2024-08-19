

number = input("Give me 5-digits number and I'll print it in reverse order: ")
if number.isdigit() and len(number) == 5:

    # converting into an integer here
    number = int(number)

    # a lil bit of math behind the scene
    ten_thousands = number // 10000
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10

    # forming a num in reverse using concatenation
    reversed_number = (
        str(units) +
        str(tens) +
        str(hundreds) +
        str(thousands) +
        str(ten_thousands)
    )

    # printing the result in reverse order
    print(reversed_number)

else:
    print("My teacher said: \n \"If the user has entered a wrong number, it's the user's problem, but not the program's.\"")