# Asks user if he/she want to play with numbers and requests a 4-digit number if yes
answer = input("Wanna play with numbers? (yes/no): ").lower()

if answer == "yes" or answer == "y":
    # Asks user for a number here
    number = input("Write a 4-digit number: ")
    # Checks if it's 4-digits and if it's a number or not
    if number.isdigit() and len(number) == 4:
        # Making an integer here
        number = int(number)
        # A lil bit of math behind the scene
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        units = number % 10

        print(thousands)
        print(hundreds)
        print(tens)
        print(units)
        result = thousands + hundreds + tens + units
        print("The total sum of your numbers is: ", result)

    else:
        print("Nce try, but I need a 4-digit number, try again")
else:
    print("Please, type \"yes\" | \"y\" if u wanna play this game")
