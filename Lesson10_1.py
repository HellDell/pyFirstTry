# let's create a generator function that will return one element of a numerical sequence,
# the law of which is set using a user function
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
    begin: 1st element of the sequence
    end: num of elements in the sequence
    func: a function that generates values for a sequence

    Yields:
    next element in the sequence
    """

    for _ in range(end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')