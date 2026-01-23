from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

l2 = []
for value, count in c.items():
    if count == 1:
        l2.append(value)
l2.sort()

print(*l2)