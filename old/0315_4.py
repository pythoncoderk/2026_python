n = int(input())
l = list(map(int, input().split()))

mx = l[0]

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]

    mx = max(mx, total)

print(mx)