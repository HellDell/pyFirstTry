# let's create a cubed nums generator
def generate_cube_numbers(end):
    # a loop that iterates over nums from 2 to the end inclusive
    for i in range(2, end + 1):
        if i ** 3 <= end:
            yield i ** 3
        else:
            return

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("OK")