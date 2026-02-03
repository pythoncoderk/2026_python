from collections import Counter

s = input()
c = Counter(s)

mx = max(c.values())
l = []
for value, count in c.items():
    if count == mx:
        l.append(value)
l.sort()
print(l[0])