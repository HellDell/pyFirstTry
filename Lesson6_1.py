# let's create a program that returns all the letters in the given interval
import string

# getting an input from user
user_input = input("Enter two characters: ").strip()

# splits user's input into two sub-strings
start, end = user_input.split('-')

# ascii shit goes here
all_letters = string.ascii_letters
start_index = all_letters.index(start)  # finding the index of the initial letter
end_index = all_letters.index(end)  # finding the index of the final letter

result = all_letters[start_index:end_index+1] # index of the last element ! inclusive !
print(result)
