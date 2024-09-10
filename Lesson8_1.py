# let's create a function that adds 1 to the list

def add_one(some_list):

    # converts each digit in the list to a str and .join all of them into a str
    number = int(''.join(str(digit) for digit in some_list))

    result = number + 1

    # splits the result into separate digits and returns a list
    return [int(digit) for digit in str(result)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
