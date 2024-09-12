# let's write a func that returns the difference between the max and min values in the list

def difference(*args):
    if not args:
        return 0

    max_value = max(args)
    min_value = min(args)

    # using round so that the number is rounded to two decimal places
    return round(max_value - min_value, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print("OK")