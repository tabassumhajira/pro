a = int(input())
s = []
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
    s.append(i)
for i in range(1,a,2 ) :
    s.append(i)
for i in range(2,a+1,2 ) :
    s.append(i)
print(len(s))
print(*s)
