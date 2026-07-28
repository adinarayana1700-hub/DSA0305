def earley_parser(s):
    count_a = s.count('a')
    count_b = s.count('b')

    if count_a == count_b and s.startswith('a') and s.endswith('b'):
        print("Accepted")
    else:
        print("Rejected")
string = input("Enter string: ")
earley_parser(string)
