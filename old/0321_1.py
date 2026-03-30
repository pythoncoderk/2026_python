h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
ans = 0
for i in range(1, h - 1):

    for j in range(1, w - 1):
        if l[i][j] != ".":
            continue
        flag = True
        for dx, dy in dirs:
            if l[i + dx][j + dy] != "#":
                flag = False
                break
        if flag:
            ans += 1
print(ans)


