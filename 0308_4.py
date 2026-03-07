n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = sum(l[:k])

for i in range(n - k + 1):
    ans = max(ans, sum(l[i:k + i]))

print(ans)