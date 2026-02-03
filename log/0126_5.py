from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mx = max(c.values())
mn = min(c.values())

print(mx - mn)