n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(n):
        if i != j:
            for q in range(n):
                if j != q and i != q:
                    if l[i] + l[j] + l[q] == k:
                        ans += 1
print(ans)