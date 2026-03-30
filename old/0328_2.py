H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

visited = [[False] * W for _ in range(H)]

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

count = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)