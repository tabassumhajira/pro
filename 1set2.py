import sys, string, math
def reduceN( s, k) :
	if k <= 0 : return s

	if s == 0 : return 10	
	p1 = reduceN(s//10, k)*10 + s%10
	p2 = reduceN(s//10, k-1)
	if p1 < p2 :
		return p1
	else :
		return p2

s,k = input().split()
s,k = int(s),int(k)
print(reduceN(s,k))
