H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

visited = [[False] * W for _ in range(H)]

def dfs(x, y):
    visited[x][y] = True
    size = 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                size += dfs(nx, ny)
    return size

ans = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == 1 and not visited[i][j]:
            ans = max(ans, dfs(i, j))

print(ans)