def second_index(text, some_str):

    first_index = text.find(some_str)
    if first_index == -1:
        return None # returns None if the substring isn't found

    # looks for the nxt instance
    secondary_index = text.find(some_str, first_index + len(some_str))
    if secondary_index == -1:
        return None  # returns None if only one instance is found
    else:
        return secondary_index

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')