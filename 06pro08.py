import sys,string, math, itertools
a = int(input())
S = []
if a==2 :
    print('3')
    print('2 1 2')
    sys.exit()
if a==3 :
    print('4')
    print('2 1 3 2')
    sys.exit()
k = a//2
for i in range(2,a+1,2) :
    S.append(i)
for i in range(1,a,2 ) :
    S.append(i)
for i in range(2,a+1,2 ) :
    S.append(i)
print(len(S))
