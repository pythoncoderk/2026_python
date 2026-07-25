import math

x, y = map(int, input().split())
k = int(input())
n = int(input())

data = []

for i in range(n):
    xi, yi, price = map(int, input().split())

    ans = (x - xi) ** 2 + (y - yi) ** 2
    data.append((ans, price))

data.sort()

total = 0
for i in range(k):
    total += data[i][1]

answer = math.floor(total / k + 0.5)
print(answer)