# Question: Find the sum of the two digit number e.g. 47  4 + 7 = 11, without using + operator

num = int(input("Enter number: "))

a = num // 10
b = num % 10

print(a + b)