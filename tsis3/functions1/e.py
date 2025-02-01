from itertools import permutations

def string_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))
        
s = input("Enter a string: ")
string_permutations(s)