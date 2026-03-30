h, w = map(int, input().split())
n = int(input())
l1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for _ in range(m)]

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1),(1, 0), (1, 1)
]

l3 = [[0] * w for _ in range(h)]

for i in range(len(l1)):
    hx = l1[i][0]-1
    wx = l1[i][1]-1
    center = l1[i][2]
    side = l1[i][3]

    for q, r in dirs:
        nx = hx +q
        ny = wx + r

        if 0 <= nx < h and 0 <= ny < w:
            if q == 0 and r == 0:
                l3[nx][ny] = center
            else:
                l3[nx][ny] = side

total = 0
for i, j in l2:
    total += l3[i-1][j-1]

print(total)