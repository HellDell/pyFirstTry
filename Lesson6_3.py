# let's create a program that calculates the result
# of multiplying its digits until the result <= 9

# creating a loop to check if our input is only contains nums
while True:
    my_str = input("Give me a positive number: ")
    if my_str.isnumeric():      # ensures that the user has entered a num
        num = int(my_str)
        if num > 0:
            while num > 9:      # a loop until we reach number 9
                result = 1      # a starting point for multiplication
                for digit in str(num):
                    result *= int(digit)
                num = result
            print("Result: ", num)
            break
        else:
            print("The number must be positive!")