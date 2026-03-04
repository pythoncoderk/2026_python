n, k = map(int, input().split())
a = list(map(int, input().split()))

cur = sum(a[:k])
mx = cur

for i in range(k, n):
    cur += a[i]
    cur -= a[i-k]
    mx = max(mx, cur)

print(mx)