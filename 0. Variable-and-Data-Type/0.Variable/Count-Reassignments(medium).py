# Question: You are given n values assigned one by one to the same variable. Print how many times the value changed.

prv = None
change = int(input("write how many time you want to change the value: "))
count = 0

for i in range(change):
    value = int(input("Enter the value: "))
    if value != prv and i != 0:
        count += 1     
    prv = value

print(f"Value changed {count} times")