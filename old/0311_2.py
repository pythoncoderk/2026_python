n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

mx = prefix[m] - prefix[0]

for i in range(n - m + 1):
    mx = max(mx, prefix[i + m] - prefix[i])

print(mx)