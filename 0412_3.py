n = int(input())
a = list(map(int, input().split()))

mx = max(a)
ans = 0
for i in a:
    if i == mx:
        ans += 1

print(ans)
