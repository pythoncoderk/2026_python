n = int(input())
l = list(map(int, input().split()))

ans = -10 ** 18

for i in range(1 << n):
    mx = -10 ** 18
    mi = 10 ** 18
    for j in range(n):
        if i & (1 << j):
            mi = min(mi, l[j])
            mx = max(mx, l[j])
    ans = max(ans, mx - mi)

print(ans)