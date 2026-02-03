from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

s = set()
for value, count in c.items():
    s.add(count)

s2 = list(s)
s2.sort(reverse=True)

target = s2[1]

ans = []
for value, count in c.items():
    if count == target:
        ans.append(value)
ans.sort()
print(ans[0])

