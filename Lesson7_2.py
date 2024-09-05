# a program that capitalizes the 1st letter and adds a period at the end of our sentence

# creating a function
def correct_sentence(text):
    # a signal where to split our sentence
    sentence = text.split(". ")

    # creating a blank list
    edited_sentences = []

    # for iterates through each sentence in the list
    for sentence in sentence:
        sentence = sentence.strip()             # removes extra spaces
        if sentence:                            # checks if a sentence != empty
            sentence = sentence.capitalize()
            if not sentence.endswith("."):
                sentence += "."

            # adds the corrected sentence to the list
            edited_sentences.append(sentence)

    # merge of corrected sentences w/ a space
    return " ".join(edited_sentences)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')