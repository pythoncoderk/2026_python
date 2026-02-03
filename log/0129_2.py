from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []
for value, count in c.items():
    if count == 2:
        ans.append(value)

ans.sort()

if ans == []:
    print(None)
else:
    print(*ans)