from collections import Counter

s = input()
c = Counter(s)

mx = max(c.values())

print(mx)