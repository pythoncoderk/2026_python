n, k = map(int, input().split())
A = list(map(int, input().split()))

cur = sum(A[:k])
mx = cur

for i in range(k, n):
    cur += A[i] - A[i-k]
    mx = max(mx, cur)

print(mx)