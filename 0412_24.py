H, W = map(int, input().split())
a = [input() for _ in range(H)]


dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = 0

for i in range(H):
    for j in range(W):
        if a[i][j] != "X":
            continue
        count = 0
        for dx, dy in dr:
            nx = i + dx
            ny = j + dy

            if 0 <= nx < H and 0 <= ny < W:
                if a[nx][ny] == "X":
                    count += 1
        if count == 4:
            ans += 1
print(ans)