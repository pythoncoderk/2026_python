from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

g = {}

for key, value in c.items():
    if value not in g:
        g[value] = []
    g[value].append(key)

print(g)

for key in sorted(g):