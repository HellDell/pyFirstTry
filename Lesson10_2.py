# let's create a function that finds the 1st word
def first_word(text):
    # search for the 1st word in a given text
    i = 0
    while i < len(text) and not text[i].isalpha():
        i += 1

    # search for the end of a word
    j = i
    while j < len(text) and (text[j].isalpha() or text[j] == "'"):
        j += 1

    return text[i:j]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
