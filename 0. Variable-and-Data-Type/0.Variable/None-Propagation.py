# Question: A function returns None. Another variable stores this result. Print whether both variables refer to the same object.

def example():
    return None

value = example()

if value == example():
    print("YES")
else:
    print("NO")