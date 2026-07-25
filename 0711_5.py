n, m = map(int, input().split())

d = {}

for i in range(n):
    x, y = map(int, input().split())
    if x not in d:
        d[x] = y
    else:
        if d[x] <= y:
            d[x] = y
l = []
for i in range(1, m+1):
    if i not in d:
        l.append(-1)
    else:
        l.append(d[i])

print(*l)