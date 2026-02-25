import sys
input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + A[i]

ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(prefix[r] - prefix[l-1])

print("\n".join(ans))