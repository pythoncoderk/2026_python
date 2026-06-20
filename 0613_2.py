n = int(input())

ans = 0

for i in range(n):
    x, y = map(str, input().split())
    if x == "add":
        ans += int(y)
    elif x == "sub":
        ans -= int(y)
    else:
        ans *= int(y)

print(ans)