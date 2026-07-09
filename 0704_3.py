x, y, l, r, a, b = map(int, input().split())
ans = 0
for i in range(a + 1, b+1):
    if i <= l or i > r:
        ans += y
    else:
        ans += x

print(ans)