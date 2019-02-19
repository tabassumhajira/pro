import sys,string
a = int(input())
m = [ int(x) for x in input().split()]
a = len(m)
if a==1 :
    print(1)
    sys.exit()
t = 0
for i in range(1,a-1) :
    if ((m[i] > m[i-1]) and (m[i] > m[i+1])) or ((m[i] < m[i-1]) and (m[i] < m[i+1])):
        t += 1
print(t)
