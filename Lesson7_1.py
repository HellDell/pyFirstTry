# creating a function that will represent a person according to the passed parameters
def say_hi(name: str, age: int):

    #v1 w/ print (won't pass unit tests)
    # print(f"Hi. My name is {name} and I'm {age} years old")

    # v2 w/ return (will pass unit tests)
    return f"Hi. My name is {name} and I'm {age} years old"

# v1 with pre-defined arguments
# say_hi(name="Alex", age=32)

# v2 asks user for an input and returns a string (will pass unit tests)
name = input("What's your name? ")
age = int(input("How old are you? "))

#unit tests
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')