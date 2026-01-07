# Question: A global variable x = 5. Inside a function, modify x using the global keyword. Print x after function execution.

x = 5

def modify():
    global x
    x = 10
    return x

modify()

print(x)