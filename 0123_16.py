from collections import Counter


n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

avg = n / len(c)
ans = []
for value, count in c.items():
    if avg < count:
        ans.append(value)
ans.sort()
print(*ans)