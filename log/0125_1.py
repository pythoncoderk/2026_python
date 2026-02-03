from collections import Counter

n = int(input())
l = list(map(int, input().split()))

c = Counter(l)

cnt = 0
for value, count in c.items():
    if count == 1:
        cnt += 1

print(cnt)