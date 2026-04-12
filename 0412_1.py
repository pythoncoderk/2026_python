import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    if i % 2 == 0:
        ans += 1

print(ans)