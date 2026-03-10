n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a[:m])
ans = s

for i in range(m, n):
    s += a[i]
    s -= a[i - m]
    ans = max(ans, s)

print(ans)