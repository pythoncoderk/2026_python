from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []
for value, count in c.items():
    if count >= 2:
        ans.append([value, count])

ans.sort(key=lambda x: (-x[1], -x[0]))
final = []
for i in ans:
    final.append(i[0])

print(*final)