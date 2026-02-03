from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []

mx = max(c.values())
for value, count in c.items():
    if mx == count:
        ans.append(value)

print(max(ans))