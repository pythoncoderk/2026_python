from collections import Counter

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l3 = []
for i in range(n):
    l3.append((l1[i], l2[i]))

c = Counter(l3)

mx = max(c.values())

ans = []
for value, count in c.items():
    if count == mx:
        ans.append(value)

ans.sort(key=lambda x: (x[0], x[1]))

print(*ans[0])