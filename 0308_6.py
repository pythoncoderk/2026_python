n, k = map(int, input().split())
l = list(map(int, input().split()))

s = sum(l[:k])
ans = s

for i in range(k, n):
    s += l[i]
    s -= l[i - k]
    ans = max(s, ans)

print(ans)