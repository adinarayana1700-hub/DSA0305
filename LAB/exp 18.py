import re
expression = input("Enter FOPC expression: ")
pattern = r'^[A-Za-z]+\([a-zA-Z]+\)(\s+(AND|OR)\s+[A-Za-z]+\([a-zA-Z]+\))*$'
if re.match(pattern, expression):
    print("Valid FOPC Expression")
else:
    print("Invalid FOPC Expression")
