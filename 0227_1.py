import sys
inputs = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
l2 = [0] * (n + 1)

for i in range(n):
    l2[i + 1] = inputs[i] + l2[i]

print(*l2)