from collections import Counter

n = int(input())
l = list(map(int, input().split()))

c = Counter(l)

mx = max(c.values())
ans = []
for value, count in c.items():
    if count == mx:
        ans.append(value)

ans.sort()
print(ans[0])