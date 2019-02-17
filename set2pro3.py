import sys, string, math
r,s = input().split()
r,s = int(r), int(s)
L = [ int(x) for x in input().split()]
for i in range(0,s) :
    m,n = input().split()
    m,n = int(m), int(n)
    print(min(L[m-1:n]))
