n, m = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    if l[i] + l[i+1] == m:
        cnt += 1

print(cnt)