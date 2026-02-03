from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

avg = n // 2

ans = []
for value, count in c.items():
    if count > avg:
        ans.append(value)

ans.sort()
print(*ans)