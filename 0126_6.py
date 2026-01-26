from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mx = max(c.values())

ans = 0
for value, count in c.items():
    if count == mx:
        ans += 1

print("Yes" if ans == 1 else "No")