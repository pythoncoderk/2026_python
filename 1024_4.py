n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = a.count(k) # 端点
for i in range(n - 1):
    if a[i] < k < a[i + 1] or a[i + 1] < k < a[i]:
        ans += 1 # そうでない点
print(ans)