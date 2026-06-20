n = int(input())

d = [[] * n for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    c = l[0]
    for j in range(1, c+1):
        x = l[j]
        d[x-1].append(i+1)

for i in range(n):
    for j in range(len(d[i])+1):
        if j == 0:
            print(len(d[i]), end=' ')
        else:
            if j != len(d[i]):
                print(d[i][j - 1], end=' ')
            else:
                print(d[i][j - 1])




