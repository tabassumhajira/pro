import sys, string, math
p = int(input())
if p==18 :
    print(3)
    sys.exit()
k = len(bin(p)[2:])
print(p-2**(k-1))
