from collections import Counter

s = input()
c = Counter(s)

ans = []
mx = max(c.values())

for value, count in c.items():
    if count == mx:
        ans.append([value, count])

ans.sort()
print(ans[0][0], ans[0][1])