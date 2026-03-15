n, k = map(int, input().split())
l = list(map(int, input().split()))

mx = -10 ** 18

for i in range(1 << n):

    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]
    if total <= k:
        mx = max(mx, total)

print(mx)