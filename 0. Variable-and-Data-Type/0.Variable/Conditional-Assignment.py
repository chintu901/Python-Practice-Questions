# Question: Assign a variable result as None if input is negative, otherwise assign the square of the number.

result = int(input("Enter the number: "))
if result < 0:
    print(None)
else:
    print(result**2)
