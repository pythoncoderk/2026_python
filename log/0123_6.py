from collections import Counter

s = input()
c = Counter(s)

mx = max(c.values())
ans = []
for value, count in c.items():
    if count == mx:
        ans.append(value)

ans.sort()
print(ans[0])