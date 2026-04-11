n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(n):
        for q in range(n):
            if i != j and j != q:
                if l[i] + l[j] + l[q] == k:
                    ans += 1
print(ans)