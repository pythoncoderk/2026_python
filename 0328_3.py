def dfs(x, y):
    visited[x][y] = True

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < H and 0 <= ny < W:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                dfs(nx, ny)
