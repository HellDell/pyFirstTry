# this func searches for common elements in 2 lists

def common_elements():
    first_set = [num for num in range(100) if num % 3 == 0]
    second_set = [num for num in range(100) if num % 5 == 0]
    return set(first_set).intersection(set(second_set))

result = common_elements()
print(result)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ok")
