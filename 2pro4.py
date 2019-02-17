import sys, string, math
r,s = input().split()
r,s = int(r), int(s)
L = [ int(x) for x in input().split()]
for i in range(0,s) :
    x = 0
    m,n = input().split()
    m,n = int(m), int(n)
    for j in range(m-1,n) :
        x = x ^ L[j]
        #print(L[j],x)
    print(x)
