from itertools import*

def abc():
    a = str(input())
    b = str(input())
    c = str(input())
    d = [a, b, c]
    for i in permutations(d):
        print(i)

abc()