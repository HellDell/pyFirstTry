# let's create a function that checks whether a number is even

def is_even(digit):
    # solving w/ usage of modulo
    if digit % 2 == 0:
        return True
    else:
        return False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')