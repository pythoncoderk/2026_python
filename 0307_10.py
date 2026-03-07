n, m = map(int, input().split())
l = list(map(int, input().split()))
total = 0
l2 = {}

for i in range(m):
    l2[i + 1] = 0

for i in range(n):
    x, y = map(int, input().split())
    l2[x] += y

for i in range(m):
    total += min(l[i], l2[i+1])

print(total)