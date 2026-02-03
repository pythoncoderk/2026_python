from collections import Counter

s = input()
c = Counter(s)

ans = []
for value, count in c.items():
    if count == 1:
        ans.append(value)
ans.sort()

for i in ans:
    print(i, end='')