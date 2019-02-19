import sys,string
a = int(input())
S = [ int(x) for x in input().split()]
a = len(S)
c = 0
for i in range(0,a-2) :
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if S[i] > S[j] > S[k] :
                c += 1
print(c)
