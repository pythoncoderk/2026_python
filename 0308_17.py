n = int(input())
l = list(map(int, input().split()))

l2 = [0] * (n + 1)
for i in range(n):
    l2[i + 1] = l2[i] + l[i]

ans = 0

for i in range(n - 3 + 1):
    ans = max(ans, l2[i + 3] - l2[i])

print(ans)