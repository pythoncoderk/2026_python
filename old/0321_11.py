h, w = map(int, input().split())
n, t = map(int, input().split())
l1 = [list(map(int, input().split())) for _ in range(n)]

l2 = [[0] * w for _ in range(h)]

for i in range(n):
    x = l1[i][0] - 1
    y = l1[i][1] - 1
    l2[x][y] += 1

ans = []
for i in range(h):
    for j in range(w):
        ans.append(l2[i][j])
ans.sort(reverse=True)
total = 0
for i in range(t):
    total += ans[i]
print(total)