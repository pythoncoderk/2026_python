n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if sum(map(int, str(i))) == k:
        cnt += 1

print(cnt)