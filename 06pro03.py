import sys, string, math
a = input()
a = a.lower()
s2 = string.ascii_lowercase
for b in s2 :
    if b not in a :
        print('no')
        sys.exit()
print('yes')
