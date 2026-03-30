n = int(input())
l = list(map(int, input().split()))

mx = l[0]

for i in range(1 << n):
    ans = 0
    for j in range(n):
        if i & (1 << j):
            ans += l[j]

    mx = max(mx, ans)

print(mx)