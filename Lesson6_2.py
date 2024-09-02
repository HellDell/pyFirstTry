# let's create number-to-date converter

# creating a loop to check if our input is only contains nums
while True:
    seconds_str = input("Give me a positive number in range 0 - 8639999: ")
    if seconds_str.isnumeric():     # ensures that the user has entered a valid num
        seconds = int(seconds_str)  # converts into int
        if seconds < 0 or seconds >= 8640000:
            print("Invalid number")
        else:
            break
    else:
        print("Invalid input. Please enter a positive integer.")

# a little math magic behind the scenes
days = seconds // (24 * 60 * 60)
seconds %= (24 * 60 * 60)
hours = seconds // (60 * 60)
seconds %= (60 * 60)
minutes = seconds // 60
seconds %= 60

# printing the result using concatenation lil bit later
result = f"{days} day" if days == 1 else f"{days} days"

# zfill only works with str that's why convertion is needed
result += f" {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(result)