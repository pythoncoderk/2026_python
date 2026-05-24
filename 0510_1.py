n, k = map(int, input().split())

l1 = []
l2 = []
for i in range(n):
    x = list(map(int, input().split()))
    l1.append(x[0])
    l2.append(x[1:])

l3 = list(map(int, input().split()))
l4 = [0] * (n+1)
for i in range(n):
    l4[i+1] = l4[i] + (l1[i] * l3[i])
k2 = 0
for i in range(n):
    if l4[i] <= k and l4[i+1] >= k:
        k2 = k - l4[i]
        y = l2[i] * l3[i]
        print(y[k2-1])
        break








