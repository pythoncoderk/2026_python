n, m = map(int, input().split())
l = list(map(int, input().split()))

ans = False

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]

    if total == m:
        ans = True

print("YES" if ans else "NO")