# Question: A variable is assigned inside an if block within a function. Print whether it exists after the block.

def example():
    c = 0
    if c == 0:
        d = 1
    
    if d == 1:
        print("Yaa!!")
    else:
        print("Naa..")

example()