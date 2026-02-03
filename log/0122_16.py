from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

max_value = max(c.values())
l2 = []
for value, count in c.items():

    if max_value - count != 0:
        l2.append([value, max_value - count])
l2.sort()
for i, j in l2:
    print(i, j)