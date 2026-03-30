n = int(input())
l = list(map(int, input().split()))

ans = 0

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]

    if total % 2 == 0:
        ans += 1

print(ans)