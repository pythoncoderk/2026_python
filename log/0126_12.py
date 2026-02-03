from collections import Counter

s = input()
c = Counter(s)

mx = max(c.values())

ans = []
for value, count in c.items():
    if mx == count:
        ans.append(value)

for i in s:
    if i not in ans:
        print(i, end="")
