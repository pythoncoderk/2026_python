import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

pos = [0] * (N + 1)
for i in range(N):
    pos[A[i]] = i

ans = 0
for i in range(2, N+1):
    if pos[i-1] >pos[i]:
        ans += 1
print(ans)
