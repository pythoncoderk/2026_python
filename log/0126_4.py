from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = 0
for value, count in c.items():
    if count % 2 != 0:
        ans += 1

print(ans)