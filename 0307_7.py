n, k = map(int, input().split())
l = list(map(int, input().split()))

left = 0
ans = 0
total = 0

for i in range(n):
    total += l[i]
    while total > k:
        total -= l[left]
        left += 1

    ans = max(ans, i - left + 1)
print(ans)