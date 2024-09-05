# let's write a program that moves all zeros to the end of the list

# lst = [0, 1, 0, -12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

# v1
# we can just sort from big to small and reverse our !changed! list
# BUT our goal is to preserve the order of all non-zero numbers
# lst.sort(reverse = True)

# v2
# here we'll try to sort it out with preservation of the order

non_zero = 0            # indicates the first element that is not 0
i  = 0                  # used to iterate over all elements

# this loop repeats until we have checked all the items in the list
while i < len(lst):     
    if lst[i] != 0:     # if the element at index i is not 0 then:
        # swap elements at indexes non_zero and i
        lst[non_zero], lst[i] = lst[i], lst[non_zero] 
        
        # increase non_zero by 1
        non_zero += 1
    
    # move to the next element in the list
    i += 1              
print(lst)
