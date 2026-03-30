n, k = map(int, input().split())
l = list(map(int, input().split()))

left = 0
total = 0
ans = 0

for right in range(n):
    total += l[right]
    while total >= k:
        ans += 1
        print("YES")
        exit()
print("NO")

