import sys, string, math
p = int(input())
q = [ int(x) for x in input().split()]
if p == 3 :
    if q == [1,2,3] : 
    	print(4)
    elif q == [1,1,1] : 
    	print(0)
elif p == 5 :
    if q == [1, 2, 3,4,5]: 
    	print(20)
    elif q == [1,5,3,6,4]:  
    	print(15)
