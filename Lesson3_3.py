# the program splits one list into two and places them in a new list

# creating your "awesome" test list
# lst = [1, 2, 3, 4, 5, 6]
lst = [1, 2, 3]
# lst = [2]
# lst = []

# finding the middle
mid = len(lst) // 2

# here goes if, else solution
if len(lst) % 2 == 0: # if the remainder is 0, then the list is even
    first_half = lst[:mid] # take elements from the beginning of the list to the mid index
    second_half = lst[mid:] # take elements from mid to the end of the list
else: # if the list is odd
    first_half = lst[:mid+1] # takes an extra element for the first part
    second_half = lst[mid+1:] # the rest goes to the second part

# resulting list with two sub-lists
result = [first_half, second_half]

print(result)
