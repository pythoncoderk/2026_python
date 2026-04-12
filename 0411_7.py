n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for q in range(j+1, n):
            if l[i] + l[j] + l[q] == k:
                ans += 1

p