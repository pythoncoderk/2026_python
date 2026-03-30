n = int(input())
l = [list(map(int, input().split())) for _ in range(n-1)]

p = 0
for i in range(n-1):
    mx = max(l[i])
    if l[p][i]