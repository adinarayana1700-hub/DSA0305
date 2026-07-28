
def parse():
    global i

    if i < len(s) and s[i] == 'a':
        i += 1

        if i < len(s) and s[i] == 'a':
            parse()

        if i < len(s) and s[i] == 'b':
            i += 1
        else:
            print("Rejected")
            exit()

s = input("Enter string: ")
i = 0

parse()

if i == len(s):
    print("Accepted")
else:
    print("Rejected")
