from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []
for value, count in c.items():
    ans.append([value, count])

ans.sort(key=lambda x: (x[1], -x[0]), reverse=True)

print(ans[0][0])