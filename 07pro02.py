import sys, string, math
def isPalin(t) :
    if len(t) == 1 : 
    	return False
    if t == t[::-1] :
    	return True
    return False

t = input()
n = len(t)
for i in range(n-1,0,-1) :
    for j in range(0,n-i) :
        i1 = j
        i2 = j+i+1
        s2 = t[i1:i2]
        if isPalin(s2) :
            print(n-len(s2))
            sys.exit()
