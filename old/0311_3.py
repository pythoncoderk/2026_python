n, k = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a[:k])
ans = s

for i in range(k, n):
    s += a[i]
    s -= a[i - k]
    ans = max(ans, s)

print(ans)