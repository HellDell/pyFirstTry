def is_palindrome(text):

    # a generator that lowers all char and filters only letters and digits
    clean_text = "".join(char.lower() for char in text if char.isalnum())

    # compares the cleaned text with its inverted version
    return clean_text == clean_text[::-1]



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")