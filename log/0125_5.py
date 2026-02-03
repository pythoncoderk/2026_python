from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mn = min(c.values())

ans = 0
for value, count in c.items():
    ans += count - mn

print(ans)