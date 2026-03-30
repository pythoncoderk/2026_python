n = int(input())

c = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        c[i][j] = row[j - i - 1]

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for cc in range(b + 1, n + 1):
            if c[a][b] + c[b][cc] < c[a][cc]:
                print("Yes")
                exit(0)
print("No")