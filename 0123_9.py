from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []
for value, count in c.items():
    if count % 2 != 0:
        ans.append(value)

ans.sort()
print(*ans)