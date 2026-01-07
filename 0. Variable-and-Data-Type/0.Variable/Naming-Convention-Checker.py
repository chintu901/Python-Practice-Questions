# Check whether a variable name follows snake_case.

name = input("Enter the variable name: ")

if "_" in name and "-" not in name:
    print("YES")
else:
    print("NO")
