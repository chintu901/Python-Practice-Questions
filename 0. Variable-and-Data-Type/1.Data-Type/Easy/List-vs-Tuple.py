# Question: You are given a sequence. Print MUTABLE if it can be modified, otherwise print IMMUTABLE.

tuple_items = (1, 2, 3)
list_items = [1, 2, 3]

tuple_items[2] = 4  # TypeError: 'tuple' object does not support item assignment
list_items[2] = 4

if tuple_items[2] == 3:
    print("Tuple is IMMUTABLE")
else:
    print("Tuple is MUTABLE")

if list_items[2] == 3:
    print("List is IMMUTABLE")
else:
    print("List is MUTABLE")

