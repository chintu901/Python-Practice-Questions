# Question: Try modifying a tuple inside a list and print the result.

a = [(1, 2), (3, 4)]
a[1][0] = 2             # TypeError: 'tuple' object does not support item assignment
print(a)