from collections import Counter

s = input()
t = input()
c1 = Counter(s)
c2 = Counter(t)

if c1 == c2:
    print("Yes")
else:
    print("No")