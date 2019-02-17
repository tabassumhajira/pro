import sys, string, math
r,s = input().split()
r,s = int(r), int(s)
L = [ int(x) for x in input().split()]
for i in range(0,s) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))
