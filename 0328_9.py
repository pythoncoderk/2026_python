H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

visited = [[False] * W for _ in range(H)]

def dfs(x, y):
    visited[x][y] = True
    perimeter = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < H and 0 <= ny < W):
            perimeter += 1
        elif grid[nx][ny] == 0:
            perimeter += 1
        elif not visited[nx][ny]:
            perimeter += dfs(nx, ny)
    return perimeter

ans = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == 1 and not visited[i][j]:
            ans += dfs(i, j)

print(ans)