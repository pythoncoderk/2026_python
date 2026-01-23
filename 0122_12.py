from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

max_count = max(c.values())

ans = []

for v, k in c.items():
    if k == max_count:
        ans.append(v)

ans.sort()
print(*ans)