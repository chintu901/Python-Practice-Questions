# You are given a string. Print VALID if it can be used as a Python variable name, otherwise print INVALID.

# Special characters
special_char = ["~", "@", "#", "$", "%", "^", "&", "*", "?", "/", "|", ">", "<", ",", ".", "-"]

# Ask for the user input
variable_name = input("Enter the variable name: ")

isValid = True

# for loop to Implement the rules for naming variables
for i in variable_name:
    if i in special_char:
        isValid = False
    elif i == " ":
        isValid = False
    elif variable_name[0].isdigit():
        isValid = False

# Check if variable is valid or not
if isValid:
    print("VALID")
else:
    print("INVALID")


