n, m = map(int, input().split())
l = list(range(1, n+1))
for i in range(m):
    x, y = map(int, input().split())
    l[x-1], l[y-1] = l[y-1], l[x-1]

print(*l)