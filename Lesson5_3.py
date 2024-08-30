# let's create a hashtag-maker
my_str = input("Give me a small sentence and I'll make a hashtag for u: ")

# red flags that we don't need in a string
punctuation = "!@#$%^&*()_+-=[]{}|;:'\\\",./<>?"

# removes punctuation and converting every word to uppercase
text = ''.join(c for c in my_str if c not in punctuation).title()

# splits a string into words and merges them without spaces
hashtag = "".join(text.split())

# adding a '#' and cutting our str to 139 char because '#' is also a char
hashtag = "#" + hashtag[:139]

print(hashtag)