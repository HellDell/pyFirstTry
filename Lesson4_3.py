# let's create a list w/ random nums AND using 3 nums from it create a new list

import random

# generate a random list with a length between 3 and 10
lst_length = random.randint(3, 10)

# creating a random num of nums
lst_random = [random.randint(0, 100) for _ in range(lst_length)]

# creating a new list with needed elements
new_lst = [lst_random[0], lst_random[2], lst_random[-2]]

print(lst_random)
print(new_lst)