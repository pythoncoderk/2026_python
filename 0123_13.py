from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

cnt = 0

mx = max(c.values())

for value, count in c.items():
    if mx == count:
        cnt += 1

print(cnt)