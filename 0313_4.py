n, k = map(int, input().split())
a = list(map(int, input().split()))

mx = -10 ** 18

for i in range(1 << n):
    s = 0
    b = []
    for j in range(n):
        if i & (1 << j):
            s += a[j]
            b.append(a[j])
    if len(b) == k:
        mx = max(mx, s)

print(mx)