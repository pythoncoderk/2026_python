from collections import Counter

n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0

for i in l:
    if i >= k:
        ans += 1

print(ans)