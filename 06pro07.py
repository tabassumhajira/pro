import sys,string, math, itertools

s, s1 = input().split()
n = len(s)
for j in range(1,0,-1) :
    #print('arr len = ', j+1)
    for i in range(0,n-j) :
        li, ri = i,j+i
        s2 = s[li:ri + 1]
        #print(li, ri, s3)
        if s2 in s1 :
            print('yes')
            sys.exit()
print('no')
