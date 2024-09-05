# let's check if given string can be the name of a variable
# access the list of all reserved keywords
import keyword

# test list
test_data = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
             "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]

# gets an input from a user:
# test_var = input("Enter a variable name: ")

# iterates through the test list
for test_var in test_data:

    # checks if the variable name is not empty
    if not test_var:
        is_valid = False
    else:
    # if the name consists of a single character, it must be an underscore or a letter
        if len(test_var) == 1:
            if not (test_var.isalpha() or test_var == "_"):
                is_valid = False
            else:
                is_valid = True
        else:
        # if the name consists of multiple characters it must start with a letter
            if not test_var[0].isalpha():
                is_valid = False
            else:
            # must be entirely lowercase, and contain only letters, numbers, and underscores
                if not (test_var.islower() and test_var.replace("_", "").isalnum()):
                    is_valid = False
                else:
                    is_valid = True
        # checks if it's a reserved keyword
        if keyword.iskeyword(test_var):
            is_valid = False
    print(is_valid)
