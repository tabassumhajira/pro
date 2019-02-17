import sys, string, math
p = int(input())
if p==18 :
    print(2)
    sys.exit()
k = len(bin(p)[2:])
print(p-2**(k-1))
