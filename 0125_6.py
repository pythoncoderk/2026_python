from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
k = int(input())

ans = 0
for value, count in c.items():
    if count == k:
        ans += 1

print(ans)