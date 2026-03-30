n = int(input())

l1 = [[0] * n for i in range(n-1)]

l2 = [list(map(int, input().split())) for _ in range(n-1)]

print(l1)
print(l2)

for i in range(1, n):
    for j in range(1, n):
        l2[i][j]

