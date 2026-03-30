n, m = map(int, input().split())
a = list(map(int, input().split()))

mx = sum(a[:m])
ans = mx

for i in range(m, n):
    ans += a[i - m]
    ans -= a[i]

    ans = max(ans, mx)

print(ans)