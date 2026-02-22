n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = [0]
x = 0
for i in range(n):
    x += l[i]
    l2.append(x)

print(*l2)