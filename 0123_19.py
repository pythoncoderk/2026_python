from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mx = max(c.values())
ans = []
for value, count in c.items():
    if mx != count:
        ans.append([value, mx - count])

ans.sort()
for i, j in ans:
    print(i, j)