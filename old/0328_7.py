n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

l1 = []
l2 = []

for i, j in l:
    l1.append(i)
    l2.append(j)

l4 = []
for i in range(1, n+1):
    total = 0
    for j in range(n):
        if i == l1[j]:
            total += 1
    l4.append(total)

l5 = []
for i in range(1, n+1):
    total = 0
    for j in range(n):
        if i == l2[j]:
            total += 1
    l5.append(total)

for i in range(m):
    print(l5[i] - l4[i])