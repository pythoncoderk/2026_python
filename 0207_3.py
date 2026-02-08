from collections import Counter

n, k = map(int, input().split())

l = []
for i in range(1, k+1):
    l.append(i)

cnt = 0

for i in range(1, n+1):
    if sum(map(int, str(i))) == k:
        cnt += 1

print(cnt)
