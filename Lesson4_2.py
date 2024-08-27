# a program to find the sum of elements with even indexes
# lst = [1, 3, 5]
lst = [0, 1, 7, 2, 4, 8]

sum_even_indexed = sum(lst[::2])    # sum takes the even elements and calculates them
last_element = lst[-1]              # take the last element from the list and assigns it to a function
final_lst = sum_even_indexed * last_element     # multiplication magic is here

print(final_lst)