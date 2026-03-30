n, k = map(int, input().split())
l = list(map(int, input().split()))

best = None
best_diff = 10 ** 18

for bit in range(1 << n):
    total = 0
    for i in range(n):
        if bit & (1 << i):
            total += l[i]

    diff = abs(total - k)

    if diff < best_diff:
        best_diff = diff
        best = total

print(best)