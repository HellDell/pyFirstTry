# let's write a func that counts the number of occurrences of words from the list in a given text

def popular_words(text, words):

    # lowercases the whole text
    text = text.lower()

    # splits the text and creates the dic
    words_in_text = text.split()
    word_counts = {}

    # counting occurrences of each word
    for word in words_in_text:
        if word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    # absence check
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0

    return word_counts

assert popular_words("When I was One I had just begun When I was Two I was nearly new",
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')