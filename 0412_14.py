H, W = map(int, input().split())
grid = [input() for _ in range(H)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j]  != "X":
            continue
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] == "X":
                    ans += 1
print(ans)