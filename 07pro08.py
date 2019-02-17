import sys,string, math

r,s = input().split()
r,s = int(r),int(s)
if s < r-s :
    print(1,s+1)
else :
    print(1,r-s)
