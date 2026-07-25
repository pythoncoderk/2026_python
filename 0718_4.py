n = int(input())
ans = 0
for i in range(n):
    x, y, z = map(str, input().split())
    x = int(x)
    y = int(y)
    if z == "keep":
        ans += y - x

print(ans)
