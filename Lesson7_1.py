
def say_hi(name: str, age: int):
    print(f"Hi, my name is {name} and I'm {age} years old")

name = input("What's your name? ")
age = int(input("How old are you? "))

say_hi(name, age)