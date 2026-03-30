n = int(input())

# 1-indexed
c = [[0] * (n + 1) for _ in range(n + 1)]

# 三角形入力を2次元配列に入れる
for i in range(1, n):
    row = list(map(int, input().split()))
    idx = 0
    for j in range(i + 1, n + 1):
        c[i][j] = row[idx]
        idx += 1

# a < b < c を全探索
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for cc in range(b + 1, n + 1):
            if c[a][b] + c[b][cc] < c[a][cc]:
                print("Yes")
                exit()

print("No")