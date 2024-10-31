s = input("Write any text in snake_case: ")

# splitting the text here
words = s.split('_')

# making all letters capital
camel_case_words = [word.capitalize() for word in words]

# combining 2 pieces here
camel_case_str = ''.join(camel_case_words)

print("Result:", camel_case_str)