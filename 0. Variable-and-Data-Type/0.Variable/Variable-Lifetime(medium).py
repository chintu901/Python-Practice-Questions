# Question: Create a variable inside a loop and try to access it after the loop. Print ACCESSIBLE or NOT ACCESSIBLE.

for i in range(1):
    value = "ACCESSIBLE"
    
if value == "ACCESSIBLE":
    print("ACCESSIBLE")
else:
    print("NOT ACCESSIBLE")