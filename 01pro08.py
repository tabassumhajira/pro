import sys, string, math
def hcf(L) :
	hcf1 = 1
	for i in range(2,min(L)+1) :
		if all([x%i==0 for x in L]) :
			hcf1 = i
	return hcf1

s,t = input().split()
s,t = int(s), int(t)
L = [ int(x) for x in input().split()]
for i in range(0,t) :
	m,n = input().split()
	m,n = int(m), int(n)
	hcf1 = hcf(L[m-1:n])
	print(hcf1)
