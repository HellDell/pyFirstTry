# a program that flips the last element of the list from the end to the beginning

# creating your "awesome" test list
# lst = [1, 2, 3, 4, 5, 6]
# lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
lst = [12, 3, 4, 10, 8]

# if the list is blank
if len(lst) == 0:
    result = [] # if the list is blank the result is also blank
elif len(lst) == 1:
    result = lst # if the list contains one element it remains the same
else:
    last_element = lst[-1]
    result = [last_element] + lst[:-1] # a new list, where the last element becomes the first

print(result)
