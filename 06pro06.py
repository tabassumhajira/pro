import sys,string, math, itertools

s,t = input().split()
s,t = int(s),int(t)
L = [ int(x) for x in input().split()]
for i in range(0,s) :
    if (86400-L[i]) >= t :
        print(i+1)
        sys.exit()
    t -= (86400-L[i])
