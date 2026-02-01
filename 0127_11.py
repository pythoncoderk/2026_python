from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
k = int(input())

ans = []
for value, count in c.items():
    if count == k:
        ans.append(value)

ans.sort(reverse=True)
print(-1 if ans == [] else ans[0])