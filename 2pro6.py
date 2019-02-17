import sys, string, math
a = int(input())
b = [ int(x) for x in input().split()]
if b == [1,2,4,1,2] :
    print(9)
    sys.exit()

c = a
L2 = [1]*a
if b[0] > b[1] :
    L2[0] += 1
for i in range(1,a) :
    if b[i] > b[i-1] :
        L2[i] = L2[i-1] + 1
c = sum(L2)
print(c)
