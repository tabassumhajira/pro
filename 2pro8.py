import sys, string, math
r,s = input().split()
r,s = int(r), int(s)
L = [ int(x) for x in input().split()]
for i in range(0,r-1) :
    for j in range(i+1,r) :
        if L[i] + L[j] == s :
            print('yes')
            sys.exit()
print('no')
