h, w, n = map(int, input().split())

stamps = []
for _ in range(n):
    stamp = [input() for _ in range(h)]
    stamps.append(stamp)

r, c = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for hx in range(h):
        line = ""
        for j in range(c):
            num = b[i][j]-1
            line += stamps[num][hx]
        print(line)