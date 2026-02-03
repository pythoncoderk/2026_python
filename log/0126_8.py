from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

mx = max(c.values())

print(mx)