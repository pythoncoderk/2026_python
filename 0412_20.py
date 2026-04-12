H, W = map(int, input().split())
a = [input() for _ in range(H)]

dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = 0

for i in range(H):
    for j in range(W):
        if a[i][j] != "X":
            continue

        ni = i + dr[i][0]
        nj = j + dr[i][1]

        if 0 <= ni < H and 0 <= nj < W:
            if a[ni][nj] == "X":
                ans += 1
print(ans)