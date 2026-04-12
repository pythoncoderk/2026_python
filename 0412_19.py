H, W = map(int, input().split())
grid = [input() for _ in range(H)]

count = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == "X":
            count += 1
print(count)

