from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

ans = []

for v, c in cnt.items():
    if c % 2 == 0:
        ans.append(v)

ans.sort()

print(*ans)
