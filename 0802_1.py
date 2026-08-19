n = int(input())
m = int(input())

ans = []
for i in range(n):
    if (m & (1 << i)) == 0:
        ans.append(i + 1)

print(*ans)