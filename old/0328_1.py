n, m = map(int, input().split())

l = []
for i in range(n):
    x = list(input())
    l.append(x)

total = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == "1":
            break
        else:
            l[i][j] = "*"


for i in range(-1, n*-1-1, -1):
    for j in range(m):
        if l[i][j] == "1":
            total += 1
        elif l[i][j] == "*":
            pass
        else:
            break
print(total)


