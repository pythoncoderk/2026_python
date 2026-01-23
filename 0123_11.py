from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mn = min(c.values())

ans = []

for value, count in c.items():
    if count == mn:
        ans.append(value)

print(ans[0])