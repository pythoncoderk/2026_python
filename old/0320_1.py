n, m = map(int, input().split())
k = int(input())
l1 = [[0] * n for _ in range(m)]
l2 = [list(map(int, input().split())) for _ in range(k)]

for i in range(len(l2)):
    x = l2[i][0]-1
    y = l2[i][1]-1

    if x - 1 >= 0 and y - 1 >= 0:
        l1[x-1][y-1] = 1
    if x - 1 >= 0 and y - 0 >= 0:
        l1[x-1][y-0] = 1
    if x - 1 >= 0 and y + 1 >= 0:
        l1[x-1][y+1] = 1

    if x + 1 >= 0 and y - 1 >= 0:
        l1[x+1][y-1] = 1
    if x + 1 >= 0 and y - 0 >= 0:
        l1[x+1][y-0] = 1
    if x + 1 >= 0 and y + 1 >= 0:
        l1[x+1][y+1] = 1

    if x + 0 >= 0 and y - 1 >= 0:
        l1[x+0][y-1] = 1
    if x + 0 >= 0 and y + 1 >= 0:
        l1[x+0][y+1] = 1

ans = k
for i in range(len(l1)):
    ans += sum(l1[i])
print(ans)


