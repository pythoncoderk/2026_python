h, w, n = map(int, input().split())
l1 = []
for i in range(h):
    lx = []
    for j in range(n):
        lx.append(input())
    l1.append(lx)

r, c = map(int, input().split())
l2 = [list(map(int, input().split())) for _ in range(r)]

print(l1)
print(l2)

for i in range(r):
    line = ""
    for j in range(c):
        xx = l2[i][j] - 1
        line += l1[xx][i]
    print(line)