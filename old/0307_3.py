n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = [0] * (n + 1)

for i in range(n):
    l2[i + 1] = l2[i] + l[i]

max_l = l2[m] - l2[0]

for i in range(n - m + 1):
    max_l = max(max_l, l2[m + i] - l2[i])

print(max_l)