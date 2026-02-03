from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
k = int(input())

ln = len(c)

ans = []
for value, count in c.items():
    ans.append([value, count])

ans.sort(key=lambda x: (-x[1], x[0]))

if ln >= k:
    print(ans[k-1][0])
else:
    print(-1)