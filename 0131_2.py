n, k = map(int, input().split())

cnt = 0
i = 0
while cnt < k:
    cnt += n + i
    i += 1

print(i-1)