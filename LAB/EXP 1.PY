import re

text = "My phone number is 9876543210"

# Match (checks from the beginning of the string)
match = re.match("My", text)

if match:
    print("Match Found:", match.group())
else:
    print("No Match")

# Search (finds the pattern anywhere in the string)
search = re.search(r"\d{10}", text)

if search:
    print("Phone Number Found:", search.group())
else:
    print("Phone Number Not Found")
