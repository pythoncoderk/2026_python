n = int(input())
l = list(map(int, input().split()))

mx = -10 ** 18

for i in range(1 << n):
    if i.bit_count() % 2 != 0:
        continue
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]

    mx = max(mx, total)

print(mx)
