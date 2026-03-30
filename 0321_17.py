n = int(input())
c = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n):
    row = list(map(int, input().split()))
    idx = 0
    for j in range(i + 1, n + 1):
        c[i][j] = row[idx]
        idx += 1

for i in range(1, n + 1):
    print(*c[i][1:])