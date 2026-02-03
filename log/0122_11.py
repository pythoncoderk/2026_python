from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = 0
max_count = max(c.values())


for v, k in c.items():
    if k == max_count:
        ans += 1

print(ans)