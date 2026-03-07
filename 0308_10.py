n, x, y = map(int, input().split())
l = list(map(int, input().split()))

l2 = [0] * (n + 1)
for i in range(n):
    l2[i + 1] = l2[i] + l[i]

print(l2[y+1] - l2[x])