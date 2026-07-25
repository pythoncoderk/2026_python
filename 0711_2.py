l = int(input())
k = int(input())
l1 = list(map(int, input().split()))

for i in range(k):
    le = int(len(l1) / 2)
    x = l1[:le]
    y = l1[le:]
    x = x[::-1]

    l1 = [d + f for d, f in zip(x, y)]

print(*l1)

