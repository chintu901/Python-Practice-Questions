# Question: A variable count exists globally. A function increments count without using global. Print what happens.

count = 10

def inc():
    count += 10
    return count

inc()
print(count)