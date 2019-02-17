import sys,string, math, itertools

s = int(input())
t = 3
a = t
while s > 0 :
    if a == 0 :
        t = 2*t
        a = t
    if s==1 :
        print(a)
        sys.exit()
    s -= 1
    a -= 1
