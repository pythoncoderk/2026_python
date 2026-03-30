h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

dirs = [
    (-1, -1),(-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
ans = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if l[i][j] != ".":
            continue
        ok = True
        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if l[ni][nj] != "#":
                ok = False
                break
        if ok:
            ans += 1
print(ans)



