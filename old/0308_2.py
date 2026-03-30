n, k = map(int, input().split())
l = list(map(int, input().split()))

left = 0
total = 0
ans = n + 1

for right in range(n):
    total += l[right]

    while total >= k:
        ans = min(ans, right - left + 1)
        total -= l[left]
        left += 1

print(0 if ans == n + 1 else ans)