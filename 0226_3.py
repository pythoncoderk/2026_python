import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + A[i]

mx = prefix[k] - prefix[0]

for i in range(n - k + 1):
    mx = max(mx, prefix[i + k] - prefix[i])

print(mx)