# Write a function that takes an argument defaulting to None. Print DEFAULT if no argument is passed.

name = "chetan"

def greet(name = None):
    if name is None:
        print("None")
    else:
        print(f"Hello, {name}")

greet(name)