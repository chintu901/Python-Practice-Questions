# Question: A global variable x = 10 exists. Inside a function, x = 20 is assigned and printed. Then print x outside the function.

x = 30  # Global variable
def local_function():
    x = 20      # Local variable
    print(x)    # Output: 20

print(x)    # Output: 30