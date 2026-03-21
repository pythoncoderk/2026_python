n, m = map(int, input().split())
l1 = [list(map(int, input().split())) for _ in range(n)]
x = int(input())
l2 = [list(map(int, input().split())) for _ in range(x)]

# print(l1)
# print(l2)

total = 0
point = 0
for i in range(len(l2)):
    x = l2[i][0]-1
    y = l2[i][1]-1

    total += abs(l1[x][y] - l1[x][point])
    point = y
print(total)

