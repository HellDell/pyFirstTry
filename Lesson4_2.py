# a program to find the sum of elements with even indexes

# lst = [1, 3, 5]
lst = [0, 1, 7, 2, 4, 8]

# sum takes the even elements and calculates them
sum_even_indexed = sum(lst[::2])

# takes the last element from the list and assigns it to a function
last_element = lst[-1]

# multiplication magic is here
final_lst = sum_even_indexed * last_element     

print(final_lst)
