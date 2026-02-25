import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + l[i]

print(prefix.count(0))

