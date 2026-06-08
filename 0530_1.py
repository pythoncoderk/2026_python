a, b = map(int, input().split())
ans = 0
while True:
    if a % b != 0:
        b = a % b
        ans += 1
    else:
        ans += 1
        break

print(ans)