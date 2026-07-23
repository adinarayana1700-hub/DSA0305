s = input("Enter a string: ")

state = 0

for ch in s:
    if ch == 'a':
        state = 1
    elif ch == 'b' and state == 1:
        state = 2
    else:
        state = 0

if state == 2:
    print("Accepted")
else:
    print("Rejected")
