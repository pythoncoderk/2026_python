from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
k = int(input())

cnt = 0
for value, count in c.items():
    if count >= 1 and count <= k:
        cnt += 1

print(cnt)