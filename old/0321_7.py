h, w, n = map(int, input().split())
l1 = [list(map(str, input().split())) for _ in range(h * n)]

print(l1)

r, c = map(int, input().split())
l2 = [list(map(int, input().split())) for _ in range(r)]

print(l2)

for i in range(r):
    ans = ""
    for j in range(h):
        ans += l1[l2[i][j]-1]